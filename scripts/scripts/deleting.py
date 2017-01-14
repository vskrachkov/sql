"""
deleting.py
===========

Basic example of deleting rows from table.

"""

from core.common import exc


def main():
    exc("DELETE FROM person "
        "WHERE first_name = 'Susan';")


if __name__ == '__main__':
    main()
