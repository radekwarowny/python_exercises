from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# python shell. built-in secrets module. secrets.token_hex(16)
app.config['SECRET_KEY'] = '693335d645d20cd5367737efc7c982c8'

post = [
    {
        'author': 'Radek Warowny',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'April 27 2021'
    },
    {
        'author': 'Conner Heckley',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 28 2021'

    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=post)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

