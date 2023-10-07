from flask import Flask, render_template, redirect, url_for, session
from database import DatabaseManager
import request
import database
import ai

app = Flask(__name__)
db_manager = DatabaseManager('')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_page():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create_post():
    name = request.form.get('name')
    emailAddress= request.form.get('emailAddress')
    password = request.form.get('password')
    school = request.form.get('school')
    courseName = request.form.get('courseName')
    lectureNotes = request.form.get('lectureNotes')
    description = request.form.get('description')

    print(f"Received for data - Name: {name}, Email: {emailAddress}")
    
    return redirect(url_for(
        'submit_page',
        name=name,
        emailAddress=emailAddress,
        password=password,
        school=school,
        courseName = courseName,
        lectureNotes = lectureNotes,
        description = description
        )
    )

@app.route('/submit', methods=['GET'])
def submit_page():
    name = request.args.get('name')
    emailAddress = request.args.get('emailAddress')
    password = request.args.get('password')
    school = request.args.get('school')
    courseName = int(request.args.get('courseName'))
    lectureNotes = int(request.args.get('lectureNotes'))
    description = int(request.args.get('description'))

    database.insert_account(name, emailAddress, password, school, courseName, lectureNotes, description)
    return render_template('submit.html', emailAddress=emailAddress)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    emailAddress = request.form.get('emailAddress')
    password = request.form.get('password')

    if database.is_account(emailAddress, password):
        session['emailAddress'] = emailAddress
        return redirect(url_for(
            'prompt_page', 
            emailAddress=emailAddress
            ))
    else: 
        return redirect(url_for('login_page'))

@app.route('/prompt', methods=['GET'])
def prompt_page():
    emailAddress = request.args.get('emailAddress')
    return render_template('prompt.html', emailAddress=emailAddress)

@app.route('/logout')
def logout():
    session.pop('emailAddress', None)
    return redirect(url_for('index'))
    

# @app.route('/ai', methods=['GET'])
# def get_prof_email():
#     email = ai.global_variable

if __name__ == '__main__':
    database.create_account_table()
    database.create_course_table()
    app.run(debug=True)
