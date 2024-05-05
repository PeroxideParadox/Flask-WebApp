#as authentication will take place here

from flask import Blueprint
from flask import render_template,request
auth=Blueprint('auth',__name__)

#for passing the values we will use the {{ inside this we can have python references}}
#by default it only accepts GET Requests 
#Whenever Request is Inside a route we get all the information passed to the server here of the form that is being used 

@auth.route('/login', methods=['POST','GET','post','get'])
def login():
    data=request.form
    print(data)
    return render_template("login.html",boolean=True)

#will change this return with actual page with the Help of Jinga
@auth.route('/signup',methods=['POST','GET'])
def signup():
    data=request.form
    print(data)
    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return render_template('login.html')
