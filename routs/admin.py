from flask import render_template, jsonify
from model import *
import random

def admin_routs(app):

    @app.route('/admin_dashbord', methods=['GET' , 'POST'])
    def admin():
        return render_template('admin.html')
    
    @app.route('/get_data', methods=['GET' , 'POST'])
    def getData():
        return jsonify()