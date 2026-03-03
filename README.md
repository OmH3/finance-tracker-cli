# Personal Finance CLI Tracker

A command-line expense and income tracker built with pure Python. No frameworks, no GUI — just clean Python.

## Features

- Add income and expense transactions
- Categorize transactions
- View all transactions
- Filter by category, date range, or amount
- Summary report with totals and statistics
- Save and load transactions from a JSON file

## Project Structure

```
finance_cli_tracker/
├── main.py        # menu loop and entry point
├── utils.py       # input validation, helpers, generator
├── storage.py     # JSON save and load
└── report.py      # summary, filters, recursion
```

## Requirements

- Python 3.11+
- No third-party libraries required

## Run

```bash
python main.py
```

## Usage

```
1. Add Transaction
2. View All
3. View Summary
4. Filter by Category
5. Filter by Date Range
6. Filter Above Amount
7. Save to File
8. Load from File
9. Exit
```

## Transaction Structure

```json
{
    "amount": 500.0,
    "type": "expense",
    "category": "food",
    "date": "2026-03-01",
    "note": "dinner"
}
```
