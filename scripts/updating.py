"""
updating.py
===========

Basic example of updating data in tables.

"""

from common import exl, exc


def main():
	"""If we omit block 'where', all rows in table will be updated."""
	exc("""
		update person
		set 
			street = '123 Tremmon St.',
			city = 'Boston',
			state = 'MA',
			country = 'USA',
			postal_code = '02345'
		where first_name = 'William';""")
	exl("""
		select person_id, first_name, last_name, birth_date
		from person;
		select person_id, food
		from favorite_food;""")


if __name__ == '__main__':
	main()