"""
tasks_11.py
==========

The following exercises are designed to consolidate the understanding
of the conditional logic.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task111(self):
        """Rewrite following query:

            SELECT emp_id,
                CASE title
                    WHEN 'President' THEN 'Management'
                    WHEN 'Vice President' THEN 'Management'
                    WHEN 'Treasurer' THEN 'Management'
                    WHEN 'Loan Manager' THEN 'Management'
                    WHEN 'Operations Manager' THEN 'Operations'
                    WHEN 'Head Teller' THEN 'Operations'
                    WHEN 'Teller' THEN 'Operations'
                    ELSE 'Unknown'
                END
            FROM employee;
        """
        self.ex("""
SELECT
    e.emp_id,
    CASE
        WHEN e.title IN ('President', 'Vice President',
                         'Treasurer', 'Loan Manager')
            THEN 'Management'
        WHEN e.title IN ('Operations Manager', 'Head Teller', 'Teller')
            THEN 'Operations'
        ELSE 'Unknown'
    END
FROM employee e""")

    def task_112(self):
        """Rewrite following query:

            SELECT open_branch_id, COUNT(*)
            FROM account
            GROUP BY open_branch_id;
        """
        self.ex("""
SELECT
    SUM(CASE WHEN open_branch_id = 1 THEN 1 END) AS branch_1,
    SUM(CASE WHEN open_branch_id = 2 THEN 1 END) AS branch_2,
    SUM(CASE WHEN open_branch_id = 3 THEN 1 END) AS branch_3,
    SUM(CASE WHEN open_branch_id = 4 THEN 1 END) AS branch_4
FROM account;""")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
