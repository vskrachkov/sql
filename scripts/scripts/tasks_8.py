"""
tasks_8.py
==========

The following exercises are designed to consolidate the understanding
of the grouping and aggregation in SQL.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task81(self):
        """Extract number of rows in account table."""
        self.ex("SELECT count(*) FROM account")

    def task82(self):
        """Extracts number of accounts for every customer."""
        self.ex(
            "SELECT count(*) accounts_count, a.cust_id "
            "FROM account a "
            "GROUP BY cust_id")

    def task83(self):
        """Extracts number of accounts for every customer that have at least
        two accounts.
        """
        self.ex(
            "SELECT count(*) accounts_count, a.cust_id "
            "FROM account a "
            "GROUP BY cust_id "
            "HAVING accounts_count >= 2")

    def task84(self):
        """Extracts sum of available balance grouped by product cd for every
        branch that has more than one account.
        """
        self.ex("SELECT product_cd, open_branch_id, sum(avail_balance) "
                "FROM account "
                "GROUP BY product_cd, open_branch_id "
                "HAVING count(*) > 1 "
                "ORDER BY 3")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
