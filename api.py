from flask_restful import Api, Resource, reqparse
from model import *

def createAPI(app):
    appApi = Api(app)
    appApi.add_resource(userAPI, '/api/userquery/<tag>/<query>')

#CRUD


# post -    C 
# get -     R 
# put -     U 
# delete -  D 



class userAPI(Resource):

    def get(self, tag, query ):
        if tag == "Song":
            raw_data=songs.query.filter_by(name = query).all()
            data = {}
            count=0

            for i in raw_data:
                data[count]= {'name': i.name}
                count+=1

        elif tag == "Artist":
            raw_data=users.query.filter_by(name = query).all()
            data = {}
            count=0

            for i in raw_data:
                for j in i.album:
                    for song_id in j.songs_list.split(','):
                        
                        raw_data2=songs.query.filter_by(id = song_id).all()

                        for song in raw_data2:
                            data[count]= {'name': song.name}
                            count+=1

        
        elif tag == "Album":
            raw_data=albums.query.filter_by(name = query).all()
            data = {}
            count=0

            for i in raw_data:
                
                for song_id in i.songs_list.split(','):
                    raw_data2=songs.query.filter_by(id = song_id).all()
                    for song in raw_data2:
                            data[count]= {'name': song.name}
                            count+=1


        return {'output': data}


