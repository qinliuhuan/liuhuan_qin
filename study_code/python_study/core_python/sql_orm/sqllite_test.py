import sqlite3

cxn = sqlite3.connect('test.db')
cur = cxn.cursor()

cur.execute('create table users(login varchar(8), uid integer )')
cur.execute('insert into users values ("john", 100)')
cur.execute('insert into users values ("jane", 150)')
cur.execute('insert into users values ("dhh", 200)')

cur.execute('select * from users')
for eachUser in cur.fetchall():
    print("eachUser: ", eachUser)


cur.execute('drop table users')

cur.close()
cxn.commit()
cxn.close()