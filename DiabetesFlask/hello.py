from markupsafe import escape
from flask import Flask, render_template, request
import pickle
import pymongo
from pymongo import MongoClient
import numpy as np

#cluster = MongoClient("mongodb://localhost:27017/firstDB")
cluster = MongoClient("mongodb://freecosmosmongo:96H8EIaveSasdyY5IIvuvml0cYXZaM9DuO536yJYLvXfUxSypKfOPigVuBPyusllTfiXPjD2FSAqIDHIF9qdfg==@freecosmosmongo.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@freecosmosmongo@")
db = cluster["firstDB"]
collection = db["c2"]

with open('model_Diabetes', 'rb') as f:
    mp = pickle.load(f)

app = Flask(__name__)


@app.route('/')
def tamim():
    return render_template("home.html")


@app.route('/predict', methods=['POST'])
def home():
    data1 = int(request.form['a'])
    data2 = int(request.form['b'])
    data3 = int(request.form['c'])
    data4 = int(request.form['d'])

    data5 = int(request.form['e'])
    data6 = float(request.form['f'])
    data7 = float(request.form['g'])
    data8 = int(request.form['h'])

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    pred = mp.predict(arr)

    if pred == 0:
        finalData = "Diabetes Negative"
    else:
        finalData = "Diabetes Positive"

    myList = [
        {"question a": data1, "question a": data1, "question b": data2, "question c": data3, "question d": data4, "question e": data5, "question f": data6, "question g": data7, "question h": data8, "Result": finalData}
    ]

    collection.insert_many(myList)

    return render_template('after.html', data=pred)


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


if __name__ == "__main__":
    app.run(debug=True)




