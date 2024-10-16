import os
from flask import Flask, render_template, request, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))
 
app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SECRETE_KEY'] = os.environ['SECRETE_KEY']
app.secret_key = os.environ['SECRETE_KEY']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    name = db.Column(db.String(100), nullable=False, primary_key=True)
    year = db.Column(db.Integer, nullable=False, primary_key=True)
    dept = db.Column(db.String(100), nullable=False, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    posting = db.Column(db.String(100), nullable=False, primary_key=True)
    status = db.Column(db.Integer, default=0, primary_key=True)
    
    def set_password(self, password):
                self.password = bcrypt.generate_password_hash(password+os.environ["SALT"]).decode("utf-8")
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password+os.environ["SALT"])

    def __repr__ (self): 
      return f"{self.name},{self.year},{self.batch},{self.dept},{self.email},{self.password},{self.phone_number},{self.posting},{self.status}"

class Admin(db.Model): 
    id = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    
    def set_password(self, password):
                self.password_hash = bcrypt.generate_password_hash(password+os.environ["SALT"]).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password+os.environ["SALT"])

    def __repr__(self): 
      return f"{self.id},{self.password}"


@app.route('/admin')
def Admin():
    return render_template("admin/Admin-layout.html")

#--------------------------------------^admin panel^--------------------------------

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        Email = request.form.get("Email")
        Password = request.form.get("pass")
        users=User().query.filter_by(email=Email).first()
        print(type(users.password),type(bcrypt.generate_password_hash(Password)))
        if users and users.check_password(Password):
            is_approve=User.query.filter_by(id=users.id).first()
            if is_approve.status == 0:
                flash('Your Account is not approved by Admin','danger')
                return redirect('/')
            else:
                session['user_id']=users.email
                session['username']=users.name
                flash('Login Successfully','success')
                return redirect('/user/dashboard')
            
        flash("Invalid credentials","danger")
        return redirect("/")
    
    return render_template("index.html") 

@app.route("/user/signup",methods=["GET","POST"])
def user_page():
    if request.method == "POST":
        Name = request.form.get("Name")
        Year = request.form.get("Year")
        Email = request.form.get("Email")
        Dept = request.form.get("Dept")
        Posting = request.form.get("Posting")
        ph_no = request.form.get("ph_no")
        Password = request.form.get("password")
        is_email=User().query.filter_by(email=Email).first()
        if is_email:
            flash('Email already Exist','danger')
            return redirect('/')
        Password = bcrypt.generate_password_hash(Password,10).decode('utf-8')
        user = User(name=Name,year=Year,dept=Dept,posting=Posting,email=Email,phone_number=ph_no,status=1)
        user.set_password(Password)
        db.session.add(user)
        db.session.commit()
        flash("Account created wait till admin approves your account!","success")
        return redirect("/")

@app.route("/user/dash",methods=["GET","POST"])
def user_dash():
    return "logged in"

if __name__ == '__main__':
    #with app.app_context :
    #db.create_all()
    app.run(debug=True,port=8080)