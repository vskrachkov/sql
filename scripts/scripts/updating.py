"""
updating.py
===========

Basic example of updating data in tables.

"""

from core.common import exc, exl


def main():
    """If we omit block 'where', all rows in table will be updated."""
    exc("""
UPDATE person
SET
    street = '123 Tremmon St.',
    city = 'Boston',
    state = 'MA',
    country = 'USA',
    postal_code = '02345'
WHERE first_name = 'William';""")
    exl("""
SELECT person_id, first_name, last_name, birth_date
FROM person;
SELECT person_id, food
FROM favorite_food;""")


if __name__ == '__main__':
    main()
