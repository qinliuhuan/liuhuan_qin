import MySQLdb

cxn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root',
                      charset='utf8',db='test')
cur = cxn.cursor()
'''run only once, the second will tell me users table already exit'''
# cur.execute('create table users(login varchar(8), uid int )')

# cur.execute("insert into users values('john', 7000)")
# cur.execute("insert into users values('jane', 9000)")
# cur.execute("insert into users values('bob', 10000)")
# name='bob'
# print(cur.execute("select * from users where login like '%s'" % name))
print(cur.execute("select * from users" ))

# for data in cur.fetchall():
#     print("%s\t%s" % data)

cur.execute("delete from users where login='bob'")
for data in cur.fetchall():
    print("%s\t%s" % data)

cur.close()
cxn.commit()
cxn.close()
