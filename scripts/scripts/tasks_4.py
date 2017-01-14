"""
tasks_4.py
==========

The following exercises are designed to consolidate the understanding 
of the filtering conditions.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task41(self):
        """Extracts transactions id, transactions date, transactions amount and
        transactions type from transaction table that are appropriate
        condition:
            'txn_date < '2005-02-26' or (txn_type_cd = 'DBT' or amount > 100)'
        """
        self.ex("SELECT txn_id, txn_date, account_id, txn_type_cd, amount "
                "FROM transaction "
                "WHERE txn_date < '2005-02-26' OR "
                "     (txn_type_cd = 'DBT' OR amount > 100);")

    def task42(self):
        """Extracts transactions id, transactions date, transactions amount and
        transactions type from transaction table that are appropriate
        condition:
        'account_id in (101,103) or not (txn_type_cd = 'DBT' or amount > 100)'
        """
        self.ex("SELECT txn_id, txn_date, account_id, txn_type_cd, amount "
                "FROM transaction "
                "WHERE account_id IN (101,103) OR "
                "      NOT (txn_type_cd = 'DBT' OR amount > 100);")

    def task43(self):
        """Extracts all accounts created in 2002."""
        self.ex("SELECT open_date "
                "FROM account "
                "WHERE open_date BETWEEN '2002-01-01' AND '2002-12-31';")

    def task44(self):
        """Extracts individual customers which have 'a' as the second letter
        in last name and letter 'e' after 'l' at any position.
        """
        self.ex("SELECT fname, lname "
                "FROM individual "
                "WHERE lname LIKE concat(`\\_`, `a`, `\\%`) AND "
                "      lname LIKE concat(`\\%`, `le`, `\\%`);")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
