#as authentication will take place here

from flask import Blueprint
from flask import render_template
auth=Blueprint('auth',__name__)

#for passing the values we will use the {{ inside this we can have python references}}
@auth.route('/login')
def login():
    return render_template("login.html")

#will change this return with actual page with the Help of Jinga
@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return "<p>Logout here</p>"
