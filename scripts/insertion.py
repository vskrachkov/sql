"""
insertion.py
============

Basic example of inserting data to table.

"""

from common import exl, exc


def insert_to_person():
	exc("""
		insert into person
			(person_id, first_name, last_name, gender, birth_date)
		values
			(null, 'William', 'Turener', 'M', '1972-05-05');

		insert into person
			(person_id, first_name, last_name, gender, birth_date,
			 street, city, state, country, postal_code)
		values
			(null, 'Susan', 'Smith', 'F', '1975-11-02', 
			 '23 Mape St.', 'Arlington', 'VA', 'USA', '20202');""")


def select_from_person():
	print('select from person')
	exl("""
		select person_id, first_name, last_name, birth_date 
		from person;""")
	print('select from person by id')
	exl("""
		select person_id, first_name, last_name, gender, birth_date
		from person
		where person_id = 1;""")


def insert_to_favorite_food():
	exc("""
		insert into favorite_food
			(person_id, food)
		values
			(1, 'cookies');

		insert into favorite_food
			(person_id, food)
		values 
			(1, 'nachos');""")


def select_from_food():
	print('select William\'s favorite foods.')
	exl("""
		select food
		from favorite_food
		where person_id = 1
		order by food;""")


def main():
	insert_to_person()
	insert_to_favorite_food()
	select_from_person()
	select_from_food()


if __name__ == '__main__':
	main()
