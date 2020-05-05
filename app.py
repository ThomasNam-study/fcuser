import os
from flask import Flask
from flask import render_template
from model import db

app = Flask(__name__)



# class Test(db.Model):
#     __tablename__ = 'test_table'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32), unique=True)
#
# db.create_all()

@app.route('/register')
def regiter():
    return render_template("register.html")

@app.route('/')
def hello_world():
    return render_template("hello.html")


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(Debug=True)
