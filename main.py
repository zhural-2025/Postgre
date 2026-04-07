from decimal import Decimal
import sys

import psycopg2

from postgres_driver import PostgresDriver


def main() -> None:
    driver = None
    try:
        driver = PostgresDriver()
        driver.create_tables()

        user_1 = driver.add_user("Alice", 28)
        user_2 = driver.add_user("Bob", 34)
        driver.add_user("Charlie", 22)  # user without orders

        driver.add_order(user_1, Decimal("499.90"))
        driver.add_order(user_2, Decimal("750.10"))
        driver.add_order(user_1, Decimal("250.00"))

        totals = driver.get_user_totals()
        print("Сумма заказов по пользователям:")
        for name, total in totals:
            print(f"{name} — {total:.2f}")

        cascade_user = driver.add_user("TempForCascade", 40)
        driver.add_order(cascade_user, Decimal("100.00"))
        before_delete = driver.count_orders_for_user(cascade_user)
        driver.delete_user(cascade_user)
        after_delete = driver.count_orders_for_user(cascade_user)
        print(
            f"Проверка ON DELETE CASCADE: до удаления заказов={before_delete}, "
            f"после удаления={after_delete}"
        )
    except psycopg2.Error as exc:
        print("Ошибка PostgreSQL:", exc, file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print("Ошибка выполнения запроса:", exc, file=sys.stderr)
        sys.exit(1)
    finally:
        if driver is not None:
            driver.close()


if __name__ == "__main__":
    main()
