from flask import render_template, request, redirect, url_for
from model import * 

def artistrouts(app):

    @app.route('/artist_dashbord', methods=['GET' , 'POST'])
    def artist_dashbord():
        return render_template("artistDashbord.html")
