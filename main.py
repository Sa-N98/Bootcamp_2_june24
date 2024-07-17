from flask import Flask, render_template, request, redirect, url_for
import os
from model import * 
from api import *
from routs.artist_routs import artistrouts
from  routs.user_routs import userrouts


current_dir =os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(current_dir,"database.sqlite3")



db.init_app(app)
app.app_context().push() # program stack

createAPI(app)




# @app.route('/', methods=["GET"]) 
# #  / = http://192.168.43.103:5000/
# def home():
#     return render_template('home.html')




@app.route('/signup', methods=['GET' , 'POST'])
def signup():
   
    if request.method == 'POST':
        username_value = request.form['username'] 
        email_value = request.form['email'] 
        password_value = request.form['password']
        user_type_value = request.form['user_type']  

        
        
        user_data= users.query.filter_by(email = email_value).first()

        if user_data == None:
            newUser = users(name = username_value,
                             email =email_value , 
                             password =password_value , 
                             user_type=user_type_value)
            db.session.add(newUser)
            db.session.commit()
            return render_template('user_added.html')
        return render_template( 'userr_notadded.html' , error_message= ' Registration Successful!', redirect_massage = 'Click here to login' )


       
        # if user_data != None:
        #     print()
        #     print("name ==>" ,user_data.name)
        #     print("email ==>" ,user_data.email)
        #     print("user type ==>" ,user_data.user_type)
        #     print()
        # else:
        #     print()
        #     print( 'user does not exists')
        #     print()


    return render_template('signup.html')



@app.route('/', methods=['GET' , 'POST'])
def login():

    if request.method == 'POST':
        
        email_value = request.form['email'] 
        password_value = request.form['password']

        user_data= users.query.filter_by(email = email_value).first()

        if user_data != None:
            if user_data.password == password_value:

                if user_data.user_type == 'commoner':
                    return  redirect(url_for('user_dashbord'))
                elif user_data.user_type == 'artist':
                    return redirect(url_for('artist_dashbord'))
                
        return render_template( 'userr_notadded.html', error_message= "User dosen't exists ", redirect_massage = 'Click here to Signup')
    return render_template('login.html')
        

userrouts(app)
artistrouts(app)


if __name__ == "__main__" :
    db.create_all()
    app.debug =True
    app.run(host='0.0.0.0')

