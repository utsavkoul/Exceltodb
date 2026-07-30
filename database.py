import sqlite3
from sqlalchemy import create_engine



engine = create_engine('sqlite:///database.db')




# cursor.execute('SELECT * FROM data')
# rows = cursor.fetchall()

# for row in rows:
#     print(row)




def insert_data(df, tablename):
    df.to_sql(tablename, con=engine, if_exists='append', index=False)

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



