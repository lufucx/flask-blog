from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '844b252766d23bec5a6a63b7ecb6d2bd'


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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', "sucess")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login Unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
