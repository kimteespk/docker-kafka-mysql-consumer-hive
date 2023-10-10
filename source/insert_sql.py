import mysql.connector
from time import sleep

user = 'confluent'
pwd = 'confluent'
port = '3306'
db_name = 'testdb'

def db_connect():
    """Function สำหรับเชื่อต่อ DB """
    global my_db
    global my_cursor
    while True:

        # user = input('User name : ')
        # pwd = getpass('Password : ')
        # user = config.user
        # pwd = config.pwd
        # port = config.port

        my_db, my_cursor = None, None
        try:
            my_db = mysql.connector.connect(
                user=user,
                password=pwd,
                port=port,
                database=db_name)
            my_cursor = my_db.cursor()
            print('Successfully connected to database')

        except Exception as e:
            print('something went wrong while attempting to connect the database.')
            if my_db is not None or my_cursor is not None:
                my_db.rollback()
            print(f'>>> Error {e}')
        if my_db is not None:
            break

db_connect()

for i in range(100):
    sql_insert = "INSERT INTO testdb2 (id, name) VALUES (%s, %s)"
    data_to_insert = (f"{i}", f'rambo{i}')
    # sql_cmd = f"INSERT INTO testdb2 (id, name) VALUES ({i}, 'rambo{i}');"
    my_cursor.execute(sql_insert, data_to_insert)
    my_db.commit()
    sleep(1)
    # break

# command_custoemr = 'SELECT * FROM testdb2'
# df_customer = pd.read_sql(command_custoemr, my_db)
# my_db = mysql.connector.connect(
#     # host= 'localhost',
#     user=user,
#     password=pwd,
#     port=port,
#     database=db_name)
# my_cursor = my_db.cursor()
# print('Successfully connected to database')
