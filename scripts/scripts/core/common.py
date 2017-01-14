import inspect

import pymysql as msql

from .config import BankDatabase, TestDatabase

try:
    con_bank = msql.connect(host=BankDatabase.HOST,
                            port=BankDatabase.PORT,
                            user='root',
                            password=BankDatabase.ROOT_PASSWORD,
                            db=BankDatabase.DATABASE)
    con_test = msql.connect(host=TestDatabase.HOST,
                            port=TestDatabase.PORT,
                            user=TestDatabase.USER,
                            password=TestDatabase.PASSWORD,
                            db=TestDatabase.DATABASE)
except msql.err.OperationalError:
    pass


def ex_(sql, con):
    """Execute sql expression.
    Parameters::
        :sql: sql expression;
        :con: mysql connector instance.
    """
    try:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
    except Exception as err:
        return err


def ex(sql, con_name=None, *sql_params):
    """Executes sql expression.
    Params::
        :sql: sql expression;
        :con_name: name of connection which will be used for
            execution expression;
        :sql_params: optional positional parameters that will be
            passed to sql expression.
    """
    if con_name == 'bank':
        with con_bank.cursor() as cur:
            cur.execute(sql, sql_params)
            return cur.fetchall()
    else:
        with con_test.cursor() as cur:
            cur.execute(sql, sql_params)
            return cur.fetchall()


def exl(sql, con_name=None, *sql_params):
    """Executes sql expression and print results in user friendly form.
    Parameters the same as in :ex: function.
    """
    for n, doc in enumerate(ex(sql, con_name=con_name, *sql_params), start=1):
        print(n, ' ' * (4 - len(str(n))), doc)


def exc(sql, con_name=None, *sql_params):
    """Executes sql expression and commit changes. Use this function
    for inserting or updating rows.
    """
    exl(sql, con_name=con_name, *sql_params)
    if con_name == 'bank':
        con_bank.commit()
    else:
        con_test.commit()


class BaseExercises:
    """The basic class for inheritance. Provides methods and properties for
    exercise execution.
    """

    def __init__(self, con_name='test', task_prefix='task'):
        self.task_prefix = task_prefix
        self.con = con_name
        self.__tasks = dict(
            inspect.getmembers(self, predicate=inspect.ismethod))

    @property
    def _tasks(self):
        """Returns a dict with all tasks."""
        return {k: v for k, v in self.__tasks.items()
                if k.startswith(self.task_prefix)}

    @property
    def _task_names(self):
        """Returns a list with all tasks."""
        return [name for name in self.__tasks.keys()
                if name.startswith(self.task_prefix)]

    @property
    def _short_task_names(self):
        """Return a list of task names without task_prefix."""
        return [name[len(self.task_prefix):] for name in self._task_names]

    def ex(self, sql):
        """Executes sql expression and prints results."""
        exl(sql, con_name=self.con)

    def main(self, message=None):
        """Run task by name.
        Parameters::
            :message: message that shows in command prompt when method called.
        """
        if not message:
            message = 'Type the task name without prefix "task" or with it' \
                      f'(availeble names: {", ".join(self._task_names)}) -> '
        task_name = input(message)
        if task_name in self._task_names:
            self._tasks[task_name]()
        elif task_name in self._short_task_names:
            print(self.task_prefix, task_name)
            self._tasks[''.join((self.task_prefix, task_name))]()
        else:
            print('No such task.')
            self.main()


def testBaseExercises():
    """Test cases for BaseExercises class."""

    class TestExercises(BaseExercises):
        def task_with_underline(self):
            print('task_with_underline')

        def task32(self):
            print('numerated tasks')

        def task(self):
            print('task')

        def task_sql(self):
            print(self.ex("select database();"))

    exercises = TestExercises(con_name='bank')
    # print(exercises._short_task_names)
    assert len(exercises._task_names) == 4
    assert exercises.task_sql() == None
    exercises.main()


if __name__ == '__main__':
    pass
    # print('All tables for test database:')
    # exl('show tables')
    # print('All tables for bank database:')
    # exl('show tables', con_name='bank')
    testBaseExercises()
