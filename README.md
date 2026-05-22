# Personal Finance Tracker 💰

A command-line tool that reads a CSV of bank transactions, categorises spending automatically, and prints a detailed monthly summary with totals per category.

**Milestone I — Python Project | ABCodes Learning Platform**

---

## What it does

- Reads a `.csv` file of bank transactions from disk
- Automatically categorises each transaction (Food, Transport, Utilities, etc.) using keyword matching
- Groups transactions by month
- Prints a clean, readable summary showing:
  - Spending per category per month
  - Total spent and total income per month
  - Net balance (surplus or deficit)
  - All-time top spending categories with a visual bar chart

---

## Project structure

```
personal-finance-tracker/
├── finance_tracker.py      # Main script
├── data/
│   └── transactions.csv    # Sample transaction data
├── requirements.txt        # Dependencies (standard library only)
└── README.md
```

---

## Requirements

- Python 3.10 or higher
- No external packages required — uses Python standard library only (`csv`, `datetime`, `collections`, `pathlib`, `sys`)

---

## Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/personal-finance-tracker.git
cd personal-finance-tracker

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

No `pip install` needed — this project uses only the standard library.

---

## Usage

### Run with the default sample data

```bash
python finance_tracker.py
```

### Run with your own CSV file

```bash
python finance_tracker.py path/to/your/transactions.csv
```

---

## CSV format

Your CSV must have these four columns (column names are case-insensitive):

| Column        | Description                        | Example              |
|---------------|------------------------------------|----------------------|
| `date`        | Transaction date                   | `2025-01-15`         |
| `description` | Merchant or transaction name       | `Shoprite Supermarket` |
| `amount`      | Transaction amount (numeric)       | `12500`              |
| `type`        | `debit` (money out) or `credit` (money in) | `debit`    |

**Supported date formats:** `YYYY-MM-DD`, `DD/MM/YYYY`, `MM/DD/YYYY`, `DD-MM-YYYY`

**Example CSV:**
```csv
date,description,amount,type
2025-01-03,Salary payment from Acme Ltd,250000,credit
2025-01-04,Shoprite Supermarket Lekki,12500,debit
2025-01-05,Uber ride to Victoria Island,3200,debit
```

---

## Categories

The tracker automatically detects these categories from transaction descriptions:

| Category              | Example keywords                           |
|-----------------------|--------------------------------------------|
| Food & Dining         | restaurant, cafe, pizza, KFC, food         |
| Groceries             | supermarket, Shoprite, Spar, market        |
| Transport             | Uber, Bolt, taxi, fuel, petrol             |
| Utilities             | electricity, DSTV, MTN, internet, data     |
| Health                | pharmacy, hospital, clinic, doctor         |
| Education             | school, course, training, book             |
| Entertainment         | cinema, Netflix, Spotify, game             |
| Shopping              | Jumia, Konga, Amazon, mall                 |
| Savings & Transfers   | transfer, savings, Cowrywise, PiggyBank    |
| Income                | salary, freelance, deposit                 |
| Uncategorized         | anything that doesn't match               |

---

## Sample output

```
┌──────────────────────────────────────────────────────────────┐
│           PERSONAL FINANCE TRACKER — MONTHLY SUMMARY          │
└──────────────────────────────────────────────────────────────┘

  ▸ JANUARY 2025
  ──────────────────────────────────────────────────────────
  CATEGORY                       SPENT      INCOME   TXN
  ──────────────────────────────────────────────────────────
  Entertainment               ₦8,500.00         —      2
  Food & Dining              ₦36,300.00         —      4
  ...
```

---

## What this project proves

> You can read real data from disk, transform it with logic, and produce structured output — the core loop of every data pipeline. Anyone can install pandas; this proves you understand what it is actually doing.

This tracker is built entirely on Python's standard library. No pandas, no shortcuts. Every transformation — parsing, categorising, grouping, formatting — is written from scratch, demonstrating genuine understanding of the data pipeline concept.

---

## Author

Benson | ABCodes Learning Platform