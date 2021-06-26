from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I need vacation'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "" or password == "":
            flash('შეიყვანეთ სწორი მონაცემები')
        else:
            u1 = Users(username=username, password=password)
            db.session.add(u1)
            db.commit()
            return "თქვენ წარმატებით გაიარეთ რეგისტრაცია"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('login.html')


@app.route('/user')
def user():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html')


if __name__ == "__main__":
    app.run(debug=True)
