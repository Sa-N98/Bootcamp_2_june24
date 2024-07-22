from flask import render_template, jsonify
from model import *
import random

import random

def admin_routs(app):

    @app.route('/admin_dashbord', methods=['GET' , 'POST'])
    def admin():
        return render_template('admin.html')
    
    @app.route('/get_data', methods=['GET' , 'POST'])
    def getData():
        artist_data= users.query.filter_by(user_type='artist').all()

        data_dictionary= dict()
        artist_name= list()
        album_count = list()
        bar_color = list()

        for i in artist_data:
            artist_name.append(i.name)
            album_count.append(len(i.album))

            r= random.randint(0,255)
            g= random.randint(0,255)
            b= random.randint(0,255)
            bar_color.append(f"rgb({r},{g},{b})")
        
        data_dictionary['artis']=artist_name
        data_dictionary['album']=album_count
        data_dictionary['color']=bar_color
        data_dictionary['total_artist']=len(artist_data)

        return jsonify(data_dictionary)