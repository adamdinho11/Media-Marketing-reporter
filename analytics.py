from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm, LoginForm
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f553f2bc13a65067e0d33e339a6de562'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    immage_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


today = str(date.today())


twitter_data = [
    {
        'username': 'shaqboss22',
        'date': today,
        'criteria': 'computer parts',
        'location': 'Trinidad'
    },
    {
        'username': 'lordtech',
        'date': today,
        'criteria': 'computer parts',
        'location': 'Santa Cruz'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', twitter_data=twitter_data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/member")
def Member():
    return render_template('member.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'adamdinho11@hotmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check username and password!', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/SignUp", methods=['GET', 'POST'])
def SignUp():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account Successfully Created for {form.username.data}! Welcome!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='SignUp', form=form)


if __name__ == '__main__':
    app.run(debug=True)
