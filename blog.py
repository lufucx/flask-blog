from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello_world():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')