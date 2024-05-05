from flask import Flask
#Setting up the database now 
from sqlalchemy import SQLAlchemy

db=SQLAlchemy()
DB_NAME="database.db"
def createapp():
    app=Flask(__name__)
    app.config['SECRETKEY']='HAKFKVSKJ FKJHFJH'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app