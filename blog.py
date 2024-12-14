from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET.KEY'] = '844b252766d23bec5a6a63b7ecb6d2bd'

posts = [
    {
        'author': 'luiz fernando',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': '14 de dezembro de 2024'
    },
    {
        'author': 'joao mauricio',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': '15 de dezembro de 2024'
    },
    {
        'author': 'caio antonio',
        'title': ' blog post 3',
        'content': 'third post content',
        'date_posted': '16 de dezembro de 2024'
    }
]

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
