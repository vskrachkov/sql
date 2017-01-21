"""
tasks_10.py
==========

The following exercises are designed to consolidate the understanding
of the outer joins.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task101(self):
        """Extracts all types of products."""
        self.ex("""
SELECT
    a.account_id AS account_id,
    pt.name      AS product_type,
    p.name       AS product_name
FROM account AS a
    RIGHT JOIN product AS p ON a.product_cd = p.product_cd
    INNER JOIN product_type AS pt ON p.product_type_cd = pt.product_type_cd
ORDER BY account_id""")

    def task102(self):
        """Extracts the same as in previous task but with using another join.
        """
        self.ex("""
SELECT
    a.account_id AS account_id,
    p.name       AS product_name
FROM product AS p
    LEFT JOIN account AS a ON p.product_cd = a.product_cd
ORDER BY account_id;""")

    def task103(self):
        """Extracts customer id, product cd and individual or business customer
         name.
         """
        self.ex("""
SELECT
    a.cust_id                     AS customer_id,
    a.product_cd                  AS product_cd,
    concat(i.fname, ' ', i.lname) AS individual_customer_name,
    b.name                        AS buisness_customer_name
FROM account AS a
    LEFT JOIN individual AS i ON a.cust_id = i.cust_id
    LEFT JOIN business AS b ON a.cust_id = b.cust_id;""")

    def task104(self):
        """Generates a set {1, 2, 3, ..., 100} using cross join."""
        self.ex("""
SELECT ones.num + tens.num + 1 AS num
FROM (SELECT 1 num
      UNION
      SELECT 2 num
      UNION
      SELECT 3 num
      UNION
      SELECT 4 num
      UNION
      SELECT 5 num
      UNION
      SELECT 6 num
      UNION
      SELECT 7 num
      UNION
      SELECT 8 num
      UNION
      SELECT 9 num
      UNION
      SELECT 0 num
     ) ones CROSS JOIN (SELECT 10 num
                        UNION
                        SELECT 20 num
                        UNION
                        SELECT 30 num
                        UNION
                        SELECT 40 num
                        UNION
                        SELECT 50 num
                        UNION
                        SELECT 60 num
                        UNION
                        SELECT 70 num
                        UNION
                        SELECT 80 num
                        UNION
                        SELECT 90 num
                        UNION
                        SELECT 0 num
                       ) tens
ORDER BY num;""")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
