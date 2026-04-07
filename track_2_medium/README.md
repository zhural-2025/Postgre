# Track 2 (Medium)

## Setup

1. Create and activate virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Create `.env` from `.env.example` and set DB credentials.

## Run

- `python main.py`

Expected result:
- totals by user from `LEFT JOIN + SUM`
- cascade check output for deleting a user with orders
