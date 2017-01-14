class Basic:
    HOST = 'localhost'
    PORT = 3306
    ROOT_PASSWORD = 'root'
    USER = 'vs'


class BankDatabase(Basic):
    DATABASE = 'bank'
    PASSWORD = 'strong_bank'


class TestDatabase(Basic):
    PORT = 3307
    DATABASE = 'test'
    PASSWORD = 'strong_test'
