# Banker

This app helps analyze PKO banking transactions by providing a grouping and a summary of transactions.

## Manual

In order to use this application:
- download transactions from your bank website for a specific month
- run app:
  - select downloaded transactions
  - select "analysis" and pick output folder
- app produces files:
  - `autogen_budget.xlsx` which contains summary of your expenses categorized into groups
  - `unmatched_transactions.html` which contains transactions that couldn't be categorized automatically 

### App Personalization
Please keep in mind that application provides best value only when it is configured according to your own needs. This can be done by modification of `categories.json` file.

This file is located in this repo, path: `src/resources/categories.json`. 

This file contains a list of categories with a:
- category name 
- payment type (can be only one of: `["household", "recurring", "occasional", "optional"]`)
- list of matching regexes (all transactions that match at least one of these regexes will be applied to this category)

When adding your own categories please pay attention to correctly specify matching regexes, as they are inside JSON file (for example you have to use double escape slash to escape a special character in regex), eg: `"EURO\\-NET"`

## Development setup

```commandline
python3 -m venv env
source env/bin/activate
pip install -e .[dev]
```