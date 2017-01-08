"""
deleting.py
===========

Basic example of deleting rows from table.

"""

from common import exc


def main():
	exc("""
		delete from person
		where first_name = 'Susan';""")

if __name__ == '__main__':
	main()