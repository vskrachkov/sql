"""
tasks_9.py
==========

The following exercises are designed to consolidate the understanding
of the subqueries.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task91(self):
        """Extracts account id, customer id and available balance
        where product type is a loan.
        """
        self.ex("SELECT account_id , cust_id, avail_balance, product_cd "
                "FROM account "
                "WHERE product_cd IN (SELECT product_cd "
                "                     FROM product "
                "                     WHERE product_type_cd='LOAN')")

    def task92(self):
        """The same task as in 91's but uses correlated subquery."""
        self.ex("SELECT a.account_id , a.cust_id, a.avail_balance, "
                "       a.product_cd "
                "FROM account AS a "
                "WHERE product_cd IN (SELECT product_cd "
                "                     FROM product AS p "
                "                     WHERE p.product_type_cd='LOAN' AND "
                "                           p.product_cd = a.product_cd)")

    def task93(self):
        """Sorts employees by their experience."""
        self.ex("""
SELECT levels.name AS experience, e.emp_id, concat(e.fname, ' ', e.lname) AS name
FROM employee e INNER JOIN
    (SELECT 'trainee' name, '2004/01/01' start_date, '2005/12/31' end_date
     UNION
     SELECT 'worker' name, '2002/01/01' start_date, '2003/12/31' end_date
     UNION
     SELECT 'mentor' name, '2000/01/01' start_date, '2001/12/31' end_date
    ) levels ON e.start_date BETWEEN levels.start_date AND levels.end_date
ORDER BY experience;""")

    def task94(self):
        """"""
        self.ex("""
SELECT
    e.emp_id                                   AS employee_id,
    concat(e.fname, ' ', e.lname)              AS name,
    (SELECT b.name
     FROM branch AS b
     WHERE b.branch_id = e.assigned_branch_id) AS branch,
    (SELECT d.name
     FROM department AS d
     WHERE d.dept_id = e.dept_id)              AS department
FROM employee AS e
ORDER BY branch;""")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
