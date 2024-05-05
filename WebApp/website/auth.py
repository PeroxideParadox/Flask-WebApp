#as authentication will take place here

from flask import Blueprint
from flask import render_template,request,flash
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
    if request.method=='post':
        email=request.form.get('email')
        firstname=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email)<4:
            flash('email must be greater than 4 characters',category='error')
        if len(firstname)<3:
            flash('it must be greater than 3 characters',category='error')
        if password1!=password2:
            flash('password do not match')  
        else:
            flash('Account created Succesfully',category='success') 
    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return render_template('login.html')
