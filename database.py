import sqlite3

ACCOUNT_DATABASE_PATH = '/Users/rachellee/Desktop/GirlsInTechHack/hackathon_climate_change/account_data.db'
COURSE_DATABASE_PATH = '/Users/rachellee/Desktop/GirlsInTechHack/hackathon_climate_change/course_data.db'

def create_account_table():
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    # Create a table for account IDs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        name TEXT NOT NULL,
        emailAddress TEXT NOT NULL,
        password TEXT NOT NULL,
        school TEXT NOT NULL,
        courseName TEXT NOT NULL,
        lectureNotes TEXT NOT NULL,
        description TEXT NOT NULL
    )
    ''')
                
    # Commit changes and close connection
    conn.commit()
    conn.close()

#insert data
def insert_account(name, email_address, password, school, courseName, lectureNotes, description):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO accounts (name, email_address, password, school, courseName, lectureNotes, description) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                   (name, email_address, password, school, courseName, lectureNotes, description))

    conn.commit()
    conn.close()

#retrieve data (format: list of tuples)
def get_accounts():
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM accounts')
    accounts = cursor.fetchall()

    conn.close()
    return accounts

def is_account(emailAddress, password):
    for tuple in get_accounts():
        if tuple[1] == emailAddress and tuple[2] == password:
            return True
    return False


def update_course_name(courseName, newName):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE accounts SET courseName = ? WHERE courseName = ?', (newName, courseName))

    conn.commit()
    conn.close()

def update_lecture_notes(lectureNotes, newNotes):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE accounts SET lectureNotes = ? WHERE lectureNotes = ?', (newNotes, lectureNotes))

    conn.commit()
    conn.close()

def update_description(description, newDescription):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE accounts SET description = ? WHERE description = ?', (newDescription, description))

    conn.commit()
    conn.close()


#course database

def create_course_table():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        courseID TEXT NOT NULL,
        corseName TEXT NOT NULL,
        description TEXT NOT NULL,
        lectureNotes TEXT NOT NULL
    )
    ''')
                
    conn.commit()
    conn.close()

#insert data
def insert_course(courseID, courseName, description, lectureNotes):
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO courses (courseID, courseName, description, lectureNotes) VALUES (?, ?, ?, ?)', 
                   (courseID, courseName, lectureNotes, description))

    conn.commit()
    conn.close()

#retrieve data (format: list of tuples)
def get_courses():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM courses')
    accounts = cursor.fetchall()

    conn.close()
    return accounts

def is_course(courseID):
    for tuple in get_courses():
        if tuple[0] == courseID:
            return True
    return False


def update_lecture_notes(lectureNotes, newNotes):
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE courses SET lectureNotes = ? WHERE lectureNotes = ?', (newNotes, lectureNotes))

    conn.commit()
    conn.close()


# get data
def get_connection():
    return sqlite3.connect(COURSE_DATABASE_PATH)

def get_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    conn.close()
    return courses

# process data
