from flask_sqlalchemy import SQLAlchemy

HOST = 'localhost'
USER = 'root'
PASSWORD = 'fran'
DB = 'app_db'

URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}'

db = SQLAlchemy()
