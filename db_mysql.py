import mysql.connector
from mysql.connector import errorcode
from organizer import Organizer

class MySQLdb(object):

    db_root_user = 'root'
    db_root_pass = 'password'
    db_host = 'local'
    cnx = mysql.connector.connect(host=db_host, user=db_root_user, password=db_root_pass)
    cursor = cnx.cursor()

    def connect_to_db(self, db_name):
        try:
            self.cursor.execute(f'USE {db_name};')
        except mysql.connector.Error as err:
            print(f'Database {db_name} does not exist.')
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                try:
                    self.cursor.execute(f'CREATE DATABASE {db_name};')
                except mysql.connector.Error as err:
                    print(f'Failed creating database {err}')
                    exit(1)

    def create_tables(self):
        tables = {}
        tables['note'] = 'CREATE TABLE notes(' \
                         '' \
                         ');'
        tables['business_card'] = 'CREATE TABLE business_card(' \
                                  '' \
                                  ');'
        tables['discount_code'] = 'CREATE TABLE discount_code(' \
                                  '' \
                                  ');'

    def insert_into_db(self, table_name, *args):
        self.cursor(f'INSERT INTO {table_name} VALUES ({args});')

    def extract_from_db(self):
        pass