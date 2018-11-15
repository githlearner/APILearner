from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'
db = SQLAlchemy(app)

class Librarydb(db.Model):
    __tablename__ = 'Library'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    author = db.Column(db.String(80))

    def __init__(self,name,author):
        self.name = name
        self.author = author

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls,name):
        result =cls.query.filter_by(name=name).first()
        return {'name':result.name}

a=Librarydb("Book","Githin")
a.save_to_db()
print(Librarydb.find_by_name("Book"))