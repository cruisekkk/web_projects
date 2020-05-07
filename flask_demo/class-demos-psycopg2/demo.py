import psycopg2

#using string composition

connection = psycopg2.connect('dbname=example')
# now we are in a session
# we can start committing these transactios

cursor = connection.cursor()
# cursor is basically an interface that allows you to start queuing up work and transactions

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))
# we can input plain string or %s, which turns this string into a template

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
    'id': 2,
    'completed': False
}
cursor.execute(SQL, data)
#result = cursor.fetchmany(1)
#print(result)

cursor.execute('SELECT * from table2;')

result = cursor.fetchmany(1)
print(result)

connection.commit()

connection.close()
cursor.close()