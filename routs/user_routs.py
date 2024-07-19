from flask import render_template, request, redirect, url_for
from model import * 

def userrouts(app):

    @app.route('/user_dashbord', methods=['GET' , 'POST'])
    def user_dashbord():
        return render_template('userDashbord.html')
    

    @app.route('/user_dashbord2', methods=['GET' , 'POST'])
    def user_dashbord2():
        return render_template('userDashbord2.html')
    
    @app.route('/user_results', methods=['GET' , 'POST'])
    def user_results():
        if request.method == 'POST':
        
            tag = request.form['tag'] 
            query = request.form['querry']

            if tag == "Song":
                raw_data=songs.query.filter_by(name = query).all()
                return render_template('results.html', data=raw_data)

            elif tag == "Artist":
                raw_data=users.query.filter_by(name = query).all()
                raw_data2= []
                for i in raw_data:
                    for j in i.album:
                        for song_id in j.songs_list.split(','):
                            
                            raw_data2.append(songs.query.filter_by(id = song_id).first())
                return render_template('results.html', data= raw_data2)


            
            elif tag == "Album":
                raw_data=albums.query.filter_by(name = query).all()
                for i in raw_data:
                    
                    for song_id in i.songs_list.split(','):
                        raw_data2=songs.query.filter_by(id = song_id).all()
                        return render_template('results.html', data= raw_data2 )




        return render_template('results.html')
    
