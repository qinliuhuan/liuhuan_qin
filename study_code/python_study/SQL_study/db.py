import sqlite3

conn = sqlite3.connect('test.db')

cur = conn.cursor()

cur.execute("create table demo(num int,str varchar(20));")
cur.execute("insert into demo values (%d, '%s')" % (1, 'aaa'))
cur.execute("insert into demo values (%d, '%s')" % (2, 'bbb'))
cur.execute("insert into demo values (%d, '%s')" % (3, 'ccc'))

cur.execute("update demo set str='%s' where num = %d" % ('ddd', 3))

cur.execute("select * from demo")
rows = cur.fetchall()
print("number of records: %s" % (len(rows)))

for i in rows:
    print (i)

conn.commit()
cur.close()
conn.close()
