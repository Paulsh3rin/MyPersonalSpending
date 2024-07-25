# My Personal Spending Analysis

## AIM
To fetch the banking data from the banks server and perform ETL and create relevant visualizations to make better financial decision and reduce unnecessary spending.

## Performing ETL

### 1. Extract:

Extracted dataset (csv) from banking server.

1. Cequing Account: "CheqMay23-June24"
2. Credit Account: "CredMay23-June24"
3. Savings Account: "SavMay23-June24"

## Data Preprocessing: 
- Added headers for each dataset
- Added feature, 'Account' within each dataset
- Used spaCy's NER capabilities to extract vendor name from transaction details. Set the cells empty for non recognized vendor names.
- Created a loop to manually enter the vendor name for empty cells.

Merge the datasets before loading
Load the data to MySQL DataBase

### 2. Required Transformations:

* Transform credit column within Credit Account (ie, seperate payments and interests)

## Issues & Solution / Flow
### Dataset
| No. | Issue / Work | Status | Description |
|-|----|-----|-----|
| 1. | No header| Resolved | add header |
| 2. | New Feature | Added | feature "Accont" |

