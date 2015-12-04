import mysql.connector
from mysql.connector import errorcode



DB_NAME = 'start'

TABLES = {}
TABLES['demo'] = (
    "CREATE TABLE `demo` ("
    "  `title` varchar(1000) NOT NULL,"
    "  `description` varchar(10000) NOT NULL,"
    "  `senRate` float NOT NULL,"
    "  `readRate` float NOT NULL,"
    "  `url` varchar(500) NOT NULL,"
    "  `category` varchar(100) NOT NULL,"
    "  `readby` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`url`)"
    ") ENGINE=InnoDB")


cnx = mysql.connector.connect(user='root',password='1111')
cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
