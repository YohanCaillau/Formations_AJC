from flask import Flask
from flask import request
import json
import pandas as pd

app = Flask(__name__) 

@app.route("/")
def main():
    return "Welcome!"

@app.route('/data')
def hello():
    return {"data": [1,2,3]}


@app.route('/csv')
def read_csv():
    csvdata = pd.read_csv('myfile.csv', sep=',', encoding="utf-8")
    data = csvdata.to_json("test.json", orient = "records")
    return data
    

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)