import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
 
app = Flask(__name__,  template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SECRETE_KEY'] = "f42235007358c148d80e28bb"

db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.String(50), nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False, primary_key=True)
    year = db.Column(db.Integer, nullable=False, primary_key=True)
    batch = db.Column(db.String(100), nullable=False, primary_key=True)
    dept = db.Column(db.String(100), nullable=False, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    posting = db.Column(db.String(100), nullable=False, primary_key=True)
    status = db.Column(db.Integer, default=0, primary_key=True)
    
    def __repr__ (): 
      return f"{self.id},{self.name},{self.year},{self.batch},{self.dept},{self.email},{self.password},{self.phone_number},{self.posting},{self.status}"

class admin(db.Model): 
    id = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(): 
      return f"{self.id},{self.password}"

@app.route('/admin')
def Admin():
    return render_template("admin/Admin-layout.html")

#--------------------------------------^admin panel^--------------------------------

@app.route('/')
def index():
    return render_template("index.html") 


if __name__ == '__main__':
    app.run(debug=True)