from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_connect_string = 'mysql://root:root@localhost:3306/test_database?charset=utf8'
ssl_args = {'ssl': {'cert': '/home//ssl/client-cert.pem',
                    'key': '/home/shouse/ssl/client-key.pem',
                    'ca': '/home/shouse/ssh/ca-cert.pem'}}
engin = create_engine(db_connect_string, connect_args=ssl_args)
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
