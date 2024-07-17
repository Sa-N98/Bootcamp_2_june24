from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()




class songs(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True ,nullable = False)
    name = db.Column(db.String)
    mp3_url = db.Column(db.String)
    album_art = db.Column(db.String)

class users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True ,nullable = False)
    name = db.Column(db.String)
    email= db.Column(db.String, unique=True)
    password= db.Column(db.String)
    user_type = db.Column(db.String)
    album = db.relationship('albums', secondary='artist_album_relationship')

class artist_album_relationship(db.Model):
    __tablename__ = "artist_album_relationship"
    artist_id =db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True,nullable = False )
    album_id =db.Column(db.Integer, db.ForeignKey("albums.id"), primary_key=True,nullable = False )

class albums(db.Model):
    __tablename__ = "albums"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True ,nullable = False)
    name = db.Column(db.String)
    songs_list = db.Column(db.String)
    artist = db.relationship('users', secondary='artist_album_relationship')