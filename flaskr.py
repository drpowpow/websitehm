import mysql.connector
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = 'db613633531.db.1and1.com'
DEBUG = True
SECRET_KEY = 'developmentkey'
USERNAME = 'dbo613633531'
PASSWORD = 'Jellopud411@'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return mysql.connector.connect(app.config['DATABASE'])

@app.route('/')
def show_entries():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
'''

Database name :	db613633531
Host name :	db613633531.db.1and1.com
Port :	3306
User name :	dbo613633531
Description :	HeartMetrics
Version :	MySQL5.5
Status :	setup started

'''