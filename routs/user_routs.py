from flask import render_template, request, redirect, url_for


def userrouts(app):

    @app.route('/user_dashbord', methods=['GET' , 'POST'])
    def user_dashbord():
        return render_template('userDashbord.html')