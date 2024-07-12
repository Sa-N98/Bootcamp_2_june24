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