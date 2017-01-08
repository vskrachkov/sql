"""
insertion.py
============

Basic examples of ALTER TABLE instruction.

"""

from common import exl


def alter_table():
	"""Alter person_id column in person table for adding auto increment.
	We need lock tables for writing, drop foreign key, modify person_id 
	in person table and than recreate foreign key.
	"""
	exl("""lock tables
			favorite_food write,
			person write;

		alter table favorite_food 
			drop foreign key fk_person_id;

		alter table person
			modify person_id smallint unsigned auto_increment;

		alter table favorite_food
			add constraint fk_person_id foreign key (person_id)

		unlock tables;""")



def main():
	alter_table()


if __name__ == '__main__':
	main()
