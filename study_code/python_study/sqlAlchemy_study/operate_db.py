import orm
from sqlalchemy import or_

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_connect_string = 'mysql://root:root@localhost:3306/test_database?charset=utf8'
# ssl_args = {'ssl': {'cert': '/home//ssl/client-cert.pem',
#                     'key': '/home/shouse/ssl/client-key.pem',
#                     'ca': '/home/shouse/ssh/ca-cert.pem'}}
# engin = create_engine(db_connect_string, connect_args=ssl_args)
engin = create_engine(db_connect_string)
SessionType = scoped_session(sessionmaker(bind=engin, expire_on_commit=False))


def GetSession():
    return SessionType()


from contextlib import contextmanager


@contextmanager
def session_scope():
    session = GetSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def InsertAccount(user, password, title, salary):
    with session_scope() as session:
        account= orm.Account(user_name=user, password=password, title=title, salary=salary)
        session.add(account)

def GetAccount(id=None, user_name=None):
    with session_scope() as session:
        return session.query(orm.Account).filter(or_(orm.Account.id == id, orm.Account.user_name == user_name)).first()

def DeleteAccount(user_name):
    with session_scope() as session:
        account = GetAccount(user_name=user_name)
        if account:
            session.delete(account)

def UpdateAccount(id, user_name, password, title, salary):
    with session_scope() as session:
        account = session.query(orm.Account).filter(orm.Account.id == id).first()
        if not account: return
        account.user_name= user_name
        account.password = password
        account.title = title
        account.salary = salary


res1 = InsertAccount("David Li", "123", "System Manager", 3000)
print("res1: ", res1)
res2 = InsertAccount("Rebeca Li", "", "Accountant", 4000)
res22 = InsertAccount("qlh", "1021", "Accountant", 12000)
print("res2: ", res2)
res3 = GetAccount(2)
print("res3: ", res3)
res4 = DeleteAccount("Howard")
print("res4: ", res4)
res5 = UpdateAccount(1, "admin", "none", "System admin", 2000)
print("res5: ", res5)


