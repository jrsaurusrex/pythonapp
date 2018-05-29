from flask import Flask, render_template, request, session, redirect, url_for
#from models import db, User
from forms import signupForm, loginForm
from flask_heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

app = Flask (__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:adminPASS@localhost/pythonAPP'
heroku = Heroku(app)
db = SQLAlchemy(app)
db.init_app(app)

############################################ Model ########################################
class User(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key = True)
    First_Name = db.Column(db.String(64))
    Last_Name = db.Column(db.String(64))
    Email = db.Column(db.String(128), unique = True)
    Pass = db.Column(db.String(64))

    def __init__(self, First_Name, Last_Name, Email, Pass):
        self.First_Name = First_Name.title()
        self.Last_Name = Last_Name.title()
        self.Email = Email.lower()
        self.set_password(Pass)

    def set_password(self, Pass):
        self.Pass = generate_password_hash(Pass)

    def check_password(self, Pass):
        return check_password_hash(self.Pass, Pass)

############################################  End Model #####################################

app.secret_key = "development-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if 'Ses' in session:
        return redirect(url_for('home'))

    form = signupForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template("signup.html", form=form)
        else:
            newuser = User(form.First_Name.data, form.Last_Name.data, form.Email.data, form.Password.data)
            db.session.add(newuser)
            db.session.commit()
            session['Ses'] = newuser.Email
            session['welcome'] = newuser.First_Name
            session['last'] = newuser.Last_Name
            return redirect(url_for('home'))

    elif request.method == "GET":
        return render_template("signup.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'Ses' in session:
        return redirect(url_for('home'))

    form = loginForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            Eemail = form.Email.data
            Password = form.Password.data

            userLog = User.query.filter_by(Email=Eemail).first()
            if userLog is not None and userLog.check_password(Password):
                session['Ses'] = form.Email.data
                session['welcome'] = userLog.First_Name
                session['last'] = userLog.Last_Name
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('Ses', None)
    session.pop('welcome', None)
    session.pop('last', None)
    return redirect(url_for('index'))


@app.route("/home")
def home():
    if 'Ses' not in session:
        return redirect(url_for('login'))
    else:
        return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
