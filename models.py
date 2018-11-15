from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def json(self):
        return {'Name':self.name,'Author':self.author}

