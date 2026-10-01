import sqlite3

import pandas as pd
from sqlalchemy import *
from pathlib import Path


# engine = create_engine('sqlite:///database.db')

# engine = create_engine('sqlite:///'+'database/'+db_file.filename)


# cursor.execute('SELECT * FROM data')
# rows = cursor.fetchall()

# for row in rows:
#     print(row)




def insert_data(df, tablename, db="database.db"):
    path = Path("./database")
    try:
        if any(path.iterdir()):
            engine = create_engine('sqlite:///' + 'database/' + db)
            print(engine)
            df.to_sql(tablename, con=engine, if_exists='append', index=False)

        else:
            return "No Database File"

    except Exception as e:
            print(f"Error occurred: {e}")

def upload_db_to_merge(db_file, table_name):
    path = Path("./database")
    if path.exists() and any(path.iterdir()):
        engine = create_engine('sqlite:///' + str(path / db_file.filename))
        df = pd.read_sql_table(table_name, con=engine)

        return df
    else:
        return "No Database File"

def select_table_data(db_file, table_name):
    pass

def insert_dictionary(dictionary_list):

    # column_names = ','.join(dictionary.keys())
    # placeholders = ','.join('?'*len(column_names))
    # values = (dictionary.values())
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS field_names (file_name, column_name, primary_key)")

    cursor.execute(f"INSERT INTO field_names (file_name, column_name, primary_key) VALUES (?, ?, ?)", dictionary_list)

    files = cursor.execute('''SELECT * FROM field_names''')
    arr = []
    for file in files:
        arr.append(file)
    print(arr)
    conn.commit()
    conn.close()
    return arr


def get_data():


    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    files = cursor.execute("SELECT * FROM field_names")
    arr=[]
    for file in files:
        arr.append(file)

    return arr



