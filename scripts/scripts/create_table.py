"""
create_table.py
===============

Basic example of table creation.
There two tables will created after running this script.

Table 'Person'
    column          type                 valid value
    ------------------------------------------------
    Person_id       Smallint (unsigned)         
    First_name      Varchar(20)
    Last_name       Varchar(20)
    Gender          Char(1)               M, F
    Birth_date      Date
    Street          Varchar(30)
    City            Varchar(20)
    State           Varchar(20)
    Country         Varchar(20)
    Postal_code     Varchar(20)

 Table 'Favorite_food'
    column          type
    --------------------
    Person_id        Smallint (unsigned)
    Food             Varchar(20)

Short description of used types:
    Date -> stores date in format yyyy-mm-dd (valid range 
        from 1000-01-01 to 9999-12-31)
    Smallint -> stores integers numbers (valid range 
        from -32 768 to 32 767 or 
        from 0 to 65 535 for marked as unsigned)
    Char -> stores string of a fixed length (filled with blanks to the right)
    Varchar -> stores string of a variable length
    //max length of *Char* and *Varchar* is the same and equals 255 symbols//

"""

from core.common import exl


def create_table_person():
    """Executes sql expresion that creates table 'person'.

    When we describe table we also need 'tell' to db server what will be
    a primary key. This makes by creating constraint for this table. In this
    case we impose constraint on the 'person_id' field and it takes 'pk_person'
    name.
    Another type of constraint is a 'check constraint', which restrict a valid
    value for the collumn. In our case:
        gender CHAR(1) CHECK (gender IN ('M', 'F')),
    MySQL allows check constraint in table definition but not checks it. But
    gives another way for do this:
        gender ENUM('M', 'F'),

    """
    sql = """CREATE TABLE `person`
    (`person_id` SMALLINT UNSIGNED,
     `first_name` VARCHAR(20),
     `last_name` VARCHAR(20),
     `gender` ENUM('M', 'F'),
     `birth_date` DATE,
     `street` VARCHAR(30),
     `city` VARCHAR(20),
     `state` VARCHAR(20),
     `country` VARCHAR(20),
     `postal_code` VARCHAR(20),
     CONSTRAINT `pk_person` PRIMARY KEY (`person_id`)
    );
    """
    exl(sql)


def create_table_favorite_food():
    """Execute sql expresion that creates table 'favorite_food'.

    Primary key of the table consist of two columns because person can have
    more then one favorite foods.
    'person_id' is a foreign key of the table, it does not allow to create
    a record with 'person_id' that does not exist in the 'person' table.
    """
    sql = """CREATE TABLE favorite_food
    (`person_id` SMALLINT UNSIGNED,
     `food` VARCHAR(20),
     CONSTRAINT `pk_favorite_food` PRIMARY KEY (`person_id`, `food`),
     CONSTRAINT `fk_person_id` FOREIGN KEY (`person_id`)
        REFERENCES `person` (`person_id`)
    );"""
    exl(sql)


def main():
    # create_table_person()
    create_table_favorite_food()


if __name__ == '__main__':
    main()
