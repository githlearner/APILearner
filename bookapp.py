from flask import Flask,request
from flask_restplus import Api,Resource,fields,reqparse
from flask_sqlalchemy import SQLAlchemy
from models import Librarydb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'
db = SQLAlchemy(app)

api = Api(app,version='1.0',title='My Library Api')
ns = api.namespace(name='Library',description= "Library Space")

book_model = api.model("book",{
    "name":fields.String("Name of the book"),
    "author":fields.String("Author of the Book"),
})

@ns.route('/books')
class Books(Resource):

    #@api.marshal_with(book_model,envelope='data')
    def get(self):
        return [x.json() for x in Librarydb.query.all()]

    @ns.expect(book_model)
    def post(self):
        data = api.payload
        name = data['name']
        author = data['author']
        if Librarydb.find_by_name(name):
            return {'Message':'Entry is already present'},400
        datatoadd = Librarydb(name,author)
        datatoadd.save_to_db()
        return {'Message':'Data added Successfully'},200

    @ns.expect(book_model)
    def put(self):
        data = api.payload
        name = data['name']
        author = data['author']
        filter = Librarydb.find_by_name(name)
        if filter:
            filter.author = author
            filter.save_to_db()
            return {'Message':'Edited successfully'},200
        return {'Message':'Error'},401

if __name__ == '__main__':
    app.run(debug =True)