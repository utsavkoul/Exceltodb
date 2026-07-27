# import sqlite3
from sqlalchemy import create_engine



engine = create_engine('sqlite:///database.db')

# conn = sqlite3.connect('Excettodb.db')

# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS data (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     age INTEGER,
#                     email TEXT
#                 )''')

# cursor.execute('''INSERT INTO data (name, age, email) VALUES
#                     ('John Doe', 30, 'john@doe.com'),
#                     ('Jane Smith', 25, 'jane@smith.com'),
#                     ('Alice Johnson', 35, 'alice@johnson.com')''')

# cursor.execute('SELECT * FROM data')
# rows = cursor.fetchall()

# for row in rows:
#     print(row)




def insert_data(df, tablename):
    df.to_sql(tablename, con=engine, if_exists='append', index=False)


# conn.commit()
# conn.close()




