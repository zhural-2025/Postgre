import os
import sys

import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError


def main() -> None:
    load_dotenv()
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "test"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
        )
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, age FROM users ORDER BY id;")
            rows = cur.fetchall()

        if not rows:
            print("Таблица users пуста.")
        else:
            print("Пользователи из users:")
            for row in rows:
                print(row)
    except OperationalError as exc:
        print("Ошибка подключения к PostgreSQL:", exc, file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print("Ошибка выполнения запроса:", exc, file=sys.stderr)
        sys.exit(1)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
