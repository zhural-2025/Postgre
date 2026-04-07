# PostgreSQL Medium Homework (Track 2)

## Quick Start

1. Create and activate virtual environment:
   - PowerShell: `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Create `.env` from `.env.example` and fill credentials.
4. Configure `.env`:
   - `DB_HOST=localhost`
   - `DB_PORT=5432`
   - `DB_NAME=test`
   - `DB_USER=postgres`
   - `DB_PASSWORD=...`

## Run

- Run script:
  - `python main.py`
- Expected output:
  - totals by user in format `Name — 1250.00`
  - cascade check message (`до удаления... после удаления...`)

## Project Files

- `main.py` - runs demo workflow for Track 2.
- `postgres_driver.py` - connection + create tables + insert + aggregate + cascade helpers.
- `requirements.txt` - dependencies (`psycopg2-binary`, `python-dotenv`).
- `.env.example` - environment variable template without secrets.
