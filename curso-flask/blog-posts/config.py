SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:@localhost:5432/blogposts_db"
#en caso de que se tenga password en la BD ---> tiger@localhost
class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    SQLALCHEMY_DATABASE_URI = POSTGRESQL

    CKEDITOR_PKG_TYPE = 'full'

    