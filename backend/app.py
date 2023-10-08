from flask import Flask, render_template, redirect, url_for, flash, request
import database
from flask import session, Flask
import sentenceBert

app = Flask(__name__, template_folder='templates')
app.secret_key = 'asecretkeyiguess'

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/signup')
def create_page():
    return render_template('signup.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/recommendations')
def rec_page():
    return render_template('recommendations.html')

@app.route('/signup', methods=['POST'])
def create_post():
    name = request.form.get('name')
    emailAddress= request.form.get('emailAddress')
    password = request.form.get('password')
    database.insert_account(name, emailAddress, password)

    print(f"Received for data - Name: {name}, Email: {emailAddress}")
    
    return redirect(url_for(
        'login_page',
        name=name,
        emailAddress=emailAddress,
        password=password
        )
    )

@app.route('/search', methods=['POST'])
def search():
    user_input = request.form.get('user_input')
    results = sentenceBert.find_similar_courses(user_input)
    return render_template('recommendations.html', results=results)


@app.route('/login', methods=['POST'])
def login_post():
    emailAddress = request.form.get('emailAddress')
    password = request.form.get('password')
    print(f"Attempting to login with: {emailAddress}, {password}")

    if database.is_account(emailAddress, password):
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard_page', emailAddress = emailAddress))
    else: 
        flash('Invalid username or password. Please try again.', 'error')
        return redirect(url_for('login_page'))


@app.route('/dashboard', methods=['GET'])
def dashboard_page():
    emailAddress = request.args.get('emailAddress')
    return render_template('dashboard.html', emailAddress=emailAddress)

@app.route('/logout')
def logout():
    session.pop('emailAddress', None)
    return redirect('/welcome')

if __name__ == '__main__':
    database.create_account_table()
    app.run(debug=True)