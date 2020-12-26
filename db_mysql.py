import mysql.connector
from mysql.connector import errorcode


class MySQLdb(object):
    db_root_user = 'root'
    db_root_pass = '****'
    db_host = 'localhost'
    cnx = mysql.connector.connect(host=db_host, user=db_root_user, password=db_root_pass)
    cursor = cnx.cursor()

    def connect_to_db(self, db_name):
        try:
            print(f'Connecting to database: ', end='')
            self.cursor.execute(f'USE {db_name}_organizer;')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print(f'DB {db_name}_organizer does not exist')
                try:
                    print(f'Creating database {db_name}_organizer: ', end='')
                    self.cursor.execute(f'CREATE DATABASE {db_name}_organizer;')
                    self.cursor.execute(f'USE {db_name}_organizer;')
                except mysql.connector.Error as err:
                    print(f'failed creating database, {err}')
                    exit(1)
                else:
                    print('created and connected')
        else:
            print('connected')

    def create_tables(self):
        tables = {}

        tables['note'] = 'CREATE TABLE note(' \
                         'id int(11) PRIMARY KEY auto_increment,' \
                         'date DATE DEFAULT(CURRENT_DATE),' \
                         'time TIME DEFAULT(CURRENT_TIME),' \
                         'title nvarchar(100) NOT NULL,' \
                         'content nvarchar(8000) NOT NULL' \
                         ');'

        tables['business_card'] = 'CREATE TABLE business_card(' \
                                  'id int(11) PRIMARY KEY auto_increment,' \
                                  'date DATE DEFAULT(CURRENT_DATE),' \
                                  'time TIME DEFAULT(CURRENT_TIME),' \
                                  'name varchar(45),' \
                                  'surname nvarchar(45),' \
                                  'mobile char(9) NOT NULL' \
                                  ');'

        tables['discount_code'] = 'CREATE TABLE discount_code(' \
                                  'id int(11) PRIMARY KEY auto_increment,' \
                                  'date DATE DEFAULT(CURRENT_DATE),' \
                                  'time TIME DEFAULT(CURRENT_TIME),' \
                                  'shop varchar(45) NOT NULL,' \
                                  'discount varchar(11) NOT NULL,' \
                                  'code varchar(30) NOT NULL' \
                                  ');'

        for table in tables:
            table_desc = tables[table]
            try:
                print(f'Creating table {table}: ', end='')
                self.cursor.execute(table_desc)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print('already exists')
                else:
                    print(err.msg)
            else:
                print('done')
        print('')

    def insert_note_into_db(self, new_note):
        insert_query = 'INSERT INTO note (title, content) ' \
                       'VALUES (%(title)s, %(content)s);'
        self.cursor.execute(insert_query, new_note)
        self.cnx.commit()

    def extract_note_from_db(self):
        select_query = 'SELECT * FROM note;'
        self.cursor.execute(select_query)
        return self.cursor

    def delete_note_from_db(self, to_be_deleted):
        delete_query = 'DELETE FROM note WHERE id = %s;'
        self.cursor.execute(delete_query, to_be_deleted)
        self.cnx.commit()


    def inser_business_card_into_db(self, data):
        insert_query = 'INSERT INTO business_card (name, surname, mobile) ' \
                       'VALUES (%s, %s, %s);'
        self.cursor.execute(insert_query, data)
        self.cnx.commit()

    def extract_business_card_from_db(self):
        select_query = 'SELECT * FROM business_card;'
        self.cursor.execute(select_query)
        return self.cursor

    def delete_business_card_from_db(self, id):
        delete_query = 'DELETE FROM business_card WHERE id = %s;'
        self.cursor.execute(delete_query, id)
        self.cnx.commit()


    def insert_discount_code_into_db(self, data):
        insert_query = 'INSERT INTO discount_code (shop, discount, code) ' \
                       'VALUES (%s, %s, %s);'
        self.cursor.execute(insert_query, data)
        self.cnx.commit()

    def extract_discount_code_from_db(self):
        select_query = 'SELECT * FROM discount_code;'
        self.cursor.execute(select_query)
        return self.cursor

    def delete_discount_code_from_db(self, id):
        delete_query = 'DELETE FROM discount_code WHERE id = %s;'
        self.cursor.execute(delete_query, id)
        self.cnx.commit()