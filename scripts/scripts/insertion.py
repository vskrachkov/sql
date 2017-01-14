"""
insertion.py
============

Basic example of inserting data to table.

"""

from core.common import exl, exc


def insert_to_person():
    exc("""
INSERT INTO person
    (person_id, first_name, last_name, gender, birth_date)
VALUES
    (NULL, 'William', 'Turner', 'M', '1972-05-05');

INSERT INTO person
    (person_id, first_name, last_name, gender, birth_date,
     street, city, state, country, postal_code)
VALUES
    (NULL, 'Susan', 'Smith', 'F', '1975-11-02',
     '23 Map St.', 'Arlington', 'VA', 'USA', '20202');""")


def select_from_person():
    print('select from person')
    exl("""
SELECT person_id, first_name, last_name, birth_date
FROM person;""")
    print('select from person by id')
    exl("""
SELECT person_id, first_name, last_name, gender, birth_date
FROM person
WHERE person_id = 1;""")


def insert_to_favorite_food():
    exc("""
INSERT INTO favorite_food
    (person_id, food)
VALUES
    (1, 'cookies');

INSERT INTO favorite_food
    (person_id, food)
VALUES
    (1, 'nachos');""")


def select_from_food():
    print('select William\'s favorite foods.')
    exl("""
SELECT food
FROM favorite_food
WHERE person_id = 1
ORDER BY food;""")


def main():
    insert_to_person()
    insert_to_favorite_food()
    select_from_person()
    select_from_food()


if __name__ == '__main__':
    main()
