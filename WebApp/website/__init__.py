from flask import Flask
#Setting up the database now 
from sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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

    from models import User,Note
    with app.app_context():
        db.create_all()
    Login_Manager=Login_Manager()
    Login_Manager.login_view='auth.login'
    Login_Manager.init_app(app)

    @Login_Manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')