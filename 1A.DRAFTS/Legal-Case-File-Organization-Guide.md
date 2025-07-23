# Legal Case File Organization Guide for macOS
## Boerner v. Rollins Case Management System

### Table of Contents
1. [Quick Reference Guide](#quick-reference-guide)
2. [Complete Naming Strategy](#complete-naming-strategy)
3. [Folder Structure](#folder-structure)
4. [Step-by-Step Implementation](#step-by-step-implementation)
5. [macOS Optimization](#macos-optimization)
6. [Examples and Templates](#examples-and-templates)

---

## Quick Reference Guide

### File Naming Format
```
YYYY-MM-DD_[CATEGORY]_[DESCRIPTION]_[VERSION].[ext]
```

### Category Codes
| Code | Type | Description |
|------|------|-------------|
| `PLG` | Pleadings | Court filings, complaints, answers |
| `EVD` | Evidence | Documents, photos, recordings |
| `COM` | Communications | Emails, letters, texts, calls |
| `LEG` | Legal Research | Statutes, case law, memos |
| `FIN` | Financial | Rent records, receipts, invoices |
| `PRO` | Property | Lease, deeds, inspections |
| `TIM` | Timeline | Chronologies, event summaries |
| `DRF` | Drafts | Work in progress documents |
| `NOT` | Notes | Meeting notes, observations |
| `ANA` | Analysis | Legal analysis, summaries |

### Folder Numbering System
- `01-` through `10-` for main categories
- Alphabetical sub-folders within each category

---

## Complete Naming Strategy

### Core Principles
1. **Date-First Format**: Always start with `YYYY-MM-DD` for chronological sorting
2. **Category Prefixes**: Use 3-letter codes for instant document type identification
3. **Descriptive Keywords**: Include searchable terms relevant to content
4. **Version Control**: Use `_v01`, `_v02`, etc. for document versions
5. **No Special Characters**: Avoid `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`
6. **Consistent Separators**: Use hyphens `-` for readability, underscores `_` for structure

### File Name Components
```
[DATE]_[CATEGORY]_[PARTY]_[SUBJECT]_[VERSION].[EXTENSION]
```

**Examples:**
- `2024-10-01_PLG_Rollins_Security-Deposit-Claim_v01.pdf`
- `2024-10-18_COM_Boerner_Dispute-Response-Letter_v02.docx`
- `2024-09-04_EVD_Property_Move-Out-Photos_v01.zip`

---

## Folder Structure

```
BOERNER-v-ROLLINS-2024/
├── 01-CASE-ADMIN/
│   ├── Case-Summary/
│   ├── Contact-Information/
│   ├── Deadlines-Calendar/
│   └── Court-Information/
├── 02-PLEADINGS-FILINGS/
│   ├── Initial-Pleadings/
│   ├── Motions/
│   ├── Responses/
│   ├── Court-Orders/
│   └── Filed-Documents/
├── 03-DISCOVERY-EVIDENCE/
│   ├── Documents/
│   ├── Photos-Video/
│   ├── Audio-Recordings/
│   ├── Expert-Reports/
│   └── Witness-Statements/
├── 04-COMMUNICATIONS/
│   ├── Email/
│   ├── Letters/
│   ├── Text-Messages/
│   ├── Phone-Logs/
│   └── Meeting-Notes/
├── 05-LEGAL-RESEARCH/
│   ├── Florida-Statutes/
│   ├── Case-Law/
│   ├── Legal-Memos/
│   └── Forms-Templates/
├── 06-FINANCIAL-RECORDS/
│   ├── Rent-Records/
│   ├── Security-Deposit/
│   ├── Receipts-Invoices/
│   └── Damage-Estimates/
├── 07-PROPERTY-RECORDS/
│   ├── Lease-Agreement/
│   ├── Property-Deeds/
│   ├── Inspection-Reports/
│   └── Maintenance-Records/
├── 08-TIMELINE-CHRONOLOGY/
│   ├── Master-Timeline/
│   ├── Event-Summaries/
│   └── Key-Dates/
├── 09-WORK-PRODUCT/
│   ├── Drafts/
│   ├── Notes/
│   ├── Analysis/
│   └── Strategy-Memos/
└── 10-ARCHIVE/
    ├── Superseded-Documents/
    ├── Duplicates/
    └── Reference-Materials/
```

---

## Step-by-Step Implementation

### Phase 1: Preparation (Day 1)
1. **Create Complete Backup**
   - Copy entire current folder to external drive
   - Name backup: `LUTH-CASE-BACKUP-YYYY-MM-DD`
   - Verify backup integrity

2. **Create New Folder Structure**
   - Create main case folder: `BOERNER-v-ROLLINS-2024`
   - Build all 10 main categories with sub-folders
   - Test folder permissions and access

### Phase 2: Document Inventory (Days 2-3)
1. **Categorize Existing Files**
   - Create spreadsheet with current file names
   - Assign category codes to each file
   - Identify duplicates and outdated versions
   - Note files requiring special attention

2. **Priority Assessment**
   - Mark critical documents (court filings, key evidence)
   - Identify time-sensitive materials
   - Flag documents needing immediate access

### Phase 3: File Migration (Days 4-6)
1. **Start with Critical Documents**
   - Move and rename court filings first
   - Handle key evidence documents
   - Process important communications

2. **Systematic Processing**
   - Work through one category at a time
   - Apply naming convention consistently
   - Verify file integrity after each move

3. **Quality Control**
   - Check renamed files open correctly
   - Verify no data corruption
   - Confirm all files accounted for

### Phase 4: Metadata Enhancement (Day 7)
1. **Add Finder Tags**
   - Apply color-coded tags by urgency
   - Add descriptive tags for content type
   - Create custom tags for case-specific terms

2. **File Comments**
   - Add brief descriptions in Get Info panel
   - Include relevant keywords
   - Note relationships between documents

### Phase 5: macOS Optimization (Day 8)
1. **Create Smart Folders**
   - Set up saved searches for document types
   - Create date-based smart folders
   - Build tag-based collections

2. **Spotlight Configuration**
   - Ensure folder is indexed
   - Test search functionality
   - Optimize search terms

### Phase 6: Testing and Refinement (Day 9)
1. **Search Testing**
   - Test various search scenarios
   - Verify Spotlight finds documents quickly
   - Check Smart Folder accuracy

2. **Workflow Testing**
   - Practice common file retrieval tasks
   - Test version control system
   - Verify backup procedures

---

## macOS Optimization

### Finder Tags Strategy
- **Red**: Urgent/Court Deadlines
- **Orange**: Pending Review
- **Yellow**: In Progress
- **Green**: Completed/Filed
- **Blue**: Reference Materials
- **Purple**: Confidential/Privileged

### Smart Folders Setup
1. **Recent Documents**: Modified within last 7 days
2. **Evidence Files**: Files tagged "Evidence"
3. **Communications**: Files in Communications folder
4. **Court Filings**: Files tagged "Court" or "Filing"
5. **This Month**: Created this month

### Spotlight Search Tips
- Use category codes: Search "EVD" for all evidence
- Date ranges: "created:2024-10-01..2024-10-31"
- File types: "kind:pdf" or "kind:image"
- Tags: "tag:urgent" or "tag:evidence"

---

## Examples and Templates

### Current vs. New Naming Examples

| Current Name | New Name |
|--------------|----------|
| `CLAIMS AGAINST LANDLORD - ALL OF THEM LISTED.md` | `2024-10-18_ANA_Boerner_Claims-Against-Landlord-Master_v02.md` |
| `TEXT MESSAGES - LEGALLY RELEVANT & MASTER TEXTS wLuther.pdf` | `2024-01-01_EVD_Luther_Text-Messages-Master-Collection_v01.pdf` |
| `83.49 Deposit money or advance rent; duty of landlord and tenant.txt` | `2024-01-01_LEG_Florida_Statute-83-49-Security-Deposits_v01.txt` |
| `EXCESSIVE GARBAGE AND TRASH IN THE FRONT AND REAR YARDS` | `2024-10-01_PLG_Rollins_Security-Deposit-Claim-Garbage_v01.pdf` |

### File Naming Templates

**Legal Documents:**
```
YYYY-MM-DD_PLG_[PARTY]_[DOCUMENT-TYPE]_v[##].[ext]
```

**Evidence Files:**
```
YYYY-MM-DD_EVD_[SOURCE]_[DESCRIPTION]_v[##].[ext]
```

**Communications:**
```
YYYY-MM-DD_COM_[FROM-TO]_[SUBJECT]_v[##].[ext]
```

**Analysis/Notes:**
```
YYYY-MM-DD_ANA_[AUTHOR]_[TOPIC]_v[##].[ext]
```

### Version Control Guidelines
- `v01`: Initial version
- `v02`: First revision
- `v03`: Second revision
- `FINAL`: Final version (use sparingly)
- `FILED`: Court-filed version

---

## Implementation Checklist

### Pre-Implementation
- [ ] Complete backup created
- [ ] New folder structure built
- [ ] File inventory spreadsheet created
- [ ] Priority documents identified

### During Implementation
- [ ] Critical documents migrated first
- [ ] Naming convention applied consistently
- [ ] File integrity verified
- [ ] Duplicates identified and handled

### Post-Implementation
- [ ] Finder tags applied
- [ ] Smart Folders created
- [ ] Search functionality tested
- [ ] Workflow procedures documented
- [ ] Team training completed (if applicable)

### Maintenance
- [ ] Weekly file organization review
- [ ] Monthly backup verification
- [ ] Quarterly system optimization
- [ ] Annual archive cleanup

---

## Troubleshooting

### Common Issues
1. **Files won't rename**: Check file permissions and close open applications
2. **Search not working**: Rebuild Spotlight index in System Preferences
3. **Tags not appearing**: Restart Finder or log out/in
4. **Smart Folders empty**: Check search criteria and folder permissions

### Best Practices
- Always work on copies when testing
- Maintain consistent naming across all files
- Regular backups before major changes
- Document any custom modifications
- Train all users on the system

---

*This guide provides a comprehensive framework for organizing legal case files on macOS. Adapt the system as needed for your specific workflow and case requirements.*