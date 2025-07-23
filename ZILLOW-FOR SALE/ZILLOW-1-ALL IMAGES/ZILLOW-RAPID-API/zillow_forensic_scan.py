import requests
import json
from datetime import datetime
import os
import time

# --- CONFIGURATION ---
# IMPORTANT: You MUST fill these out for the script to work.
# 1. Get your API Key from RapidAPI: https://rapidapi.com/apidojo/api/zillow-com1
API_KEY = "YOUR_API_KEY_HERE"  # <--- REPLACE THIS

# 2. Define the search location. A city/state or zip code is best.
LOCATION = "Houston, TX"  # <--- REPLACE THIS (e.g., "Houston, TX" or "90210")

# 3. Define the status of properties you want to track.
# Options: "ForSale", "ForRent", "Sold" (recently sold)
STATUS_TYPE = "ForSale"

# --- API DETAILS (Usually do not need to change) ---
API_HOST = "zillow-com1.p.rapidapi.com"
API_URL = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}

# --- DIRECTORY FOR SAVING DATA ---
DATA_DIR = "zillow_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def fetch_all_pages_for_location(location, status):
    """Fetches all pages of current listings for a given location and status."""
    all_props = []
    page = 1
    print(f"Starting fetch for '{location}' with status '{status}'...")
    
    while True:
        params = {
            "location": location,
            "status_type": status,
            "page": str(page)
        }
        
        try:
            response = requests.get(API_URL, headers=HEADERS, params=params)
            # Check for common user errors first
            if response.status_code == 401 or response.status_code == 403:
                print("\n--- CRITICAL ERROR ---")
                print("Authentication failed (Status Code 401/403).")
                print("Please check that your API_KEY is correct and your RapidAPI subscription is active.")
                return None
            
            response.raise_for_status()  # Raise an error for other bad status codes (4xx, 5xx)
            
            data = response.json()
            
            # The API returns an empty `props` list when there are no more results
            props = data.get("props", [])
            if not props:
                print(f"No more properties found on page {page}. Fetch complete.")
                break
            
            all_props.extend(props)
            print(f"Page {page}: Fetched {len(props)} properties. Total so far: {len(all_props)}")
            
            page += 1
            time.sleep(1.5)  # Be respectful of API rate limits

        except requests.exceptions.RequestException as e:
            print(f"\n--- ERROR ---")
            print(f"An error occurred while calling the API on page {page}: {e}")
            print(f"Response Body: {response.text if 'response' in locals() else 'No response'}")
            return None # Stop execution on error
        
    return all_props


def load_all_historical_snapshots():
    """Loads all previously saved snapshots into a single dictionary keyed by zpid."""
    historical_data = {}
    print("\nLoading historical data from local snapshots...")
    
    snapshot_files = [f for f in os.listdir(DATA_DIR) if f.startswith("snapshot_") and f.endswith(".json")]
    
    if not snapshot_files:
        print("No historical snapshots found. This must be the first run.")
        return historical_data

    for filename in sorted(snapshot_files): # Sort to process in chronological order
        filepath = os.path.join(DATA_DIR, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                # The data is a list of property dicts
                for prop in data:
                    if 'zpid' in prop:
                        # This will overwrite older data with newer, which is fine
                        historical_data[prop['zpid']] = prop
            print(f"Loaded {os.path.basename(filepath)}")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load or parse {filename}: {e}")
            
    print(f"Total unique historical properties loaded: {len(historical_data)}")
    return historical_data


def compare_snapshots(current_props, historical_props):
    """
    Compares the current snapshot with historical data to find changes.
    Returns a dictionary with new, removed, and updated listings.
    """
    print("\nComparing current snapshot with historical data...")
    current_ids = {prop['zpid'] for prop in current_props}
    historical_ids = set(historical_props.keys())
    
    new_listing_ids = current_ids - historical_ids
    removed_listing_ids = historical_ids - current_ids
    
    # Find properties that exist in both snapshots to check for updates
    potential_updates_ids = current_ids.intersection(historical_ids)
    
    changes = {
        "new_listings": [prop for prop in current_props if prop['zpid'] in new_listing_ids],
        "removed_listings": [historical_props[zpid] for zpid in removed_listing_ids],
        "price_changes": [],
        "status_changes": []
    }
    
    # Check for price and status changes
    for zpid in potential_updates_ids:
        # Find the full current property object
        current_prop = next((p for p in current_props if p['zpid'] == zpid), None)
        historical_prop = historical_props[zpid]

        if not current_prop: continue

        # Check for price change
        if current_prop.get('price') != historical_prop.get('price'):
            changes['price_changes'].append({
                "zpid": zpid,
                "address": current_prop.get('address'),
                "old_price": historical_prop.get('price'),
                "new_price": current_prop.get('price')
            })

        # Check for status change (e.g., from 'FOR_SALE' to 'PENDING')
        if current_prop.get('listingStatus') != historical_prop.get('listingStatus'):
            changes['status_changes'].append({
                "zpid": zpid,
                "address": current_prop.get('address'),
                "old_status": historical_prop.get('listingStatus'),
                "new_status": current_prop.get('listingStatus')
            })

    print(f"Analysis Complete: Found {len(changes['new_listings'])} new, {len(changes['removed_listings'])} removed, "
          f"{len(changes['price_changes'])} price changes, and {len(changes['status_changes'])} status changes.")

    return changes


def save_json_file(data, filename_prefix):
    """Saves data to a JSON file with a timestamp in the data directory."""
    if not data:
        print(f"No data to save for '{filename_prefix}'.")
        return
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.json"
    filepath = os.path.join(DATA_DIR, filename)
    
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Successfully saved data to '{filepath}'")
    except Exception as e:
        print(f"Error saving file '{filepath}': {e}")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Basic check to ensure user has configured the script
    if "YOUR_API_KEY_HERE" in API_KEY or "YOUR_LOCATION_HERE" in LOCATION:
        print("\n--- CONFIGURATION INCOMPLETE ---")
        print("Please open the script and replace 'YOUR_API_KEY_HERE' and 'YOUR_LOCATION_HERE' with your actual details.")
        exit()

    # Step 1: Fetch the current state of the market
    current_properties = fetch_all_pages_for_location(LOCATION, STATUS_TYPE)
    
    # If API fetch fails, stop execution
    if current_properties is None:
        print("\nExecution halted due to API fetch failure.")
        exit()
    
    # Save this run's data as a new snapshot
    if current_properties:
        save_json_file(current_properties, "snapshot")
    else:
        print("No current properties were fetched. Cannot perform analysis.")
        exit()

    # Step 2: Load all historical data from previous runs
    historical_properties_map = load_all_historical_snapshots()

    # Step 3: Compare current data with historical data and find changes
    if historical_properties_map:
        market_changes = compare_snapshots(current_properties, historical_properties_map)
        
        # Step 4: Save the detected changes to a file for review
        if any(market_changes.values()):
            save_json_file(market_changes, "changes_report")
        else:
            print("No changes detected since the last run.")
    else:
        print("\nThis is the first successful run. A baseline snapshot has been created.")
        print("Run the script again later to detect changes against this baseline.")
    
    print("\n--- Forensic Scan Complete ---")