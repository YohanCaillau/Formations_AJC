#print('coucou')
from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"


"""

import mysql.connector
conn = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='test')
c = conn.cursor ()

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    id= request.form('id')
    name= request.form('name')
    c.execute("CREATE TABLE IF NOT EXISTS customer (id int, name varchar(10))")
    c.execute("INSERT INTO customer(id, name) VALUES (%s,%s)", (id, name))
    conn.commit()
    return 'Done'

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    add_data()
    return render_template('template.html')

if __name__== "__main__":

   app.run('0.0.0.0',port=5000)