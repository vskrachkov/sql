"""
tasks_3.py
==========

The following exercises are designed to consolidate the understanding
of the 'select' expression and its blocks.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):

    def task31(self):
        """Extracts from the database id, name and family name of
        all bank employees
        """
        print(' ' * 5, 'emp_id, fname, lname')
        self.ex("SELECT emp_id, fname, lname "
                "FROM employee;")

    def task32(self):
        """Extracts from database account id, customer id and pending balance
        of all accounts that have status 'ACTIVE' and pending balance more
        than 2500.
        """
        print(' ' * 5, 'account_id, cust_id, pending_balance')
        self.ex("SELECT account_id, cust_id, pending_balance "
                "FROM account "
                "WHERE status = 'ACTIVE' AND pending_balance > 2500;")

    def task33(self):
        """Extracts from database distinct id of employees that have open
        balance. Take in mind that DISTINCT operation is a heavy operation
        avoid it.
        """
        print(' ' * 5, 'open_emp_id')
        self.ex("SELECT DISTINCT open_emp_id FROM account;")

    def task34(self):
        """Extracts from database product cd, customer id and available balance
        where inner join between product and account tables based
        on product cd.
        """
        print(' ' * 5, 'product_cd', 'cust_id', 'avail_balance')
        self.ex("SELECT p.product_cd, a.cust_id, a.avail_balance "
                "FROM product p INNER JOIN account a "
                "    ON p.product_cd = a.product_cd "
                "WHERE p.product_type_cd = 'ACCOUNT'")


def main():
    e = Exercises(con_name='bank')
    e.main()


if __name__ == '__main__':
    main()
