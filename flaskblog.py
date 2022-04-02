from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRECT_KEY'] = 'acfc0b77f1b5971d8152d01ae6c90ecfe667f2cd918401a16e5f9a592161dedb'

# import secrects
# secrects.token_hex(16)

posts = [
    {
        'author': 'jacky yao',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 28, 2022'
    },
    {
        'author': 'jacky yao',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 28, 2022'
    }
]

@app.route("/")
def hello():
    return "<h1>hello world!</h1>"

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
