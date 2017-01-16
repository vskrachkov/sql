"""
tasks_6.py
==========

The following exercises are designed to consolidate the understanding
of the operations on sets.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task61(self):
        """Available set A = {L M N O P} and set B = {P Q R S T}.
        What is the result of following operations:
            * A union B
            * A union all B
            * A intersect B
            * A except B

        Results:
            * {L M N O P} union {P Q R S T} = {L M N O P Q R S T}
            * {L M N O P} union {P Q R S T} = {L M N O P P Q R S T}
            * {L M N O P} intersect {P Q R S T} = {P}
            * {L M N O P} except {P Q R S T} = {L M N O}
        """
        print(self.task61.__doc__)

    def task62(self):
        """Extracts first names and last names of all individual customers and
        first names and second names of all employees.
        """
        self.ex("SELECT fname, lname, 'customer' "
                "FROM individual "
                "UNION ALL "
                "SELECT fname, lname, 'employee'"
                "FROM employee")

    def task63(self):
        """Sorts results of task62 by 'lname' column."""
        self.ex("SELECT fname, lname, 'customer' "
                "FROM individual "
                "UNION ALL "
                "SELECT fname, lname, 'employee'"
                "FROM employee "
                "ORDER BY lname")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
