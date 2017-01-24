"""
tasks_5.py
==========

The following exercises are designed to consolidate the understanding
of the inner joins between tables and self-joins.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task51(self):
        """"""
        self.ex("SELECT e.emp_id, e.fname, e.lname, b.name "
                "FROM employee e INNER JOIN branch b "
                "   ON e.assigned_branch_id = b.branch_id;")

    def task52(self):
        """Extracts account id, federal id and product name of
        individual customers.
        """
        self.ex("SELECT a.account_id, c.fed_id, p.name "
                "FROM customer c INNER JOIN account a"
                "    ON c.cust_id = a.cust_id"
                "    INNER JOIN product p"
                "    ON a.product_cd = p.product_cd")

    def task53(self):
        """Extracts all employees whose superiors assigned to another branch.
        """
        self.ex("SELECT e.emp_id, e.fname, e.lname "
                "FROM employee e INNER JOIN employee s"
                "    ON e.superior_emp_id = s.emp_id "
                "WHERE e.dept_id != s.dept_id;")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
