# PostgreSQL Basic Homework

## Quick Start

1. Create and activate virtual environment:
   - PowerShell: `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Create `.env` from `.env.example` and fill credentials.
4. Ensure PostgreSQL database `test` has table `public.users` with test rows.

## Run

- Run script:
  - `python main.py`
- Expected output:
  - rows from `SELECT id, name, age FROM users ORDER BY id;`

## Project Files

- `main.py` - connects to PostgreSQL via `.env`, reads users, closes connection in `finally`.
- `requirements.txt` - dependencies (`psycopg2-binary`, `python-dotenv`).
- `.env.example` - environment variable template without secrets.
