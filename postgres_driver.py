import os
from decimal import Decimal

import psycopg2
from dotenv import load_dotenv


class PostgresDriver:
    def __init__(self) -> None:
        load_dotenv()
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "test"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
        )

    def close(self) -> None:
        if self.conn is not None:
            self.conn.close()

    def create_tables(self) -> None:
        users_sql = """
        CREATE TABLE IF NOT EXISTS users (
          id   SERIAL PRIMARY KEY,
          name TEXT NOT NULL,
          age  INT CHECK (age >= 0)
        );
        """
        orders_sql = """
        CREATE TABLE IF NOT EXISTS orders (
          id         SERIAL PRIMARY KEY,
          user_id    INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
          amount     NUMERIC(10,2) NOT NULL,
          created_at TIMESTAMP DEFAULT NOW()
        );
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(users_sql)
                cur.execute(orders_sql)

    def add_user(self, name: str, age: int) -> int:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;",
                    (name, age),
                )
                user_id = cur.fetchone()[0]
        return user_id

    def add_order(self, user_id: int, amount: Decimal) -> int:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO orders (user_id, amount) VALUES (%s, %s) RETURNING id;",
                    (user_id, amount),
                )
                order_id = cur.fetchone()[0]
        return order_id

    def get_user_totals(self) -> list[tuple[str, Decimal]]:
        query = """
        SELECT u.name,
               COALESCE(SUM(o.amount), 0) AS total_amount
        FROM users u
        LEFT JOIN orders o ON o.user_id = u.id
        GROUP BY u.id, u.name
        ORDER BY total_amount DESC;
        """
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def count_orders_for_user(self, user_id: int) -> int:
        with self.conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM orders WHERE user_id = %s;", (user_id,))
            return cur.fetchone()[0]

    def delete_user(self, user_id: int) -> None:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
