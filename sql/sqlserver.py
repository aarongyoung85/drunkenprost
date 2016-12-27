from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile(app.config['PATH_TO_INSTANCE_CONFIG'])

def _generate_engine(db_settings):
    db_url = app.config['DB_URL'] % db_settings
    engine = create_engine(db_url, 
                    echo=False, 
                    poolclass=NullPool, 
                    encoding=app.config['DB_ENCODING'], 
                    convert_unicode=False)

    return engine

def _generate_session(db_settings):
    engine = _generate_engine(db_settings)
    Session = sessionmaker(bind=engine)

    return Session()

def DrunkenProstServer():
    db_settings = {
        'host': app.config['DB_HOST'],
        'db': app.config['DB_DATABASE'],
        'user': app.config['DB_USER'],
        'password': app.config['DB_PASSWORD'],
        'encoding': app.config['DB_ENCODING'],
    }

    return _generate_session(db_settings)
