"""
tasks_7.py
==========

The following exercises are designed to consolidate the understanding
of the some build-in functions.

"""

from core.common import BaseExercises


class Exercises(BaseExercises):
    def task71(self):
        """Returns symbols from 17 to 25 of
        'Please find the substring in this string' sting.
        """
        self.ex("SELECT SUBSTRING('Please find the substring in this string'"
                " FROM 17 FOR 9);")

    def task72(self):
        """Returns sign, absolute value and rounded value to second digit
        of '–25.76823' number
        """
        self.ex("SELECT SIGN(–25.76823), ABS(–25.76823), ROUND(–25.76823, 2);")

    def task73(self):
        """Returns only month of current date."""
        self.ex("select month(now());")


if __name__ == '__main__':
    e = Exercises(con_name='bank')
    e.main()
