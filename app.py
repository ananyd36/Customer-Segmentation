import sys
import os
from flask import Flask, redirect, render_template,request
import numpy as np 
import pandas as pd
import pickle
import requests

app = Flask(__name__)
model = pickle.load(open('segment2.pkl', 'rb'))

final_dict = {1:"A",2:"B",3:"C",4:"D"}

@app.route("/")
def home():
    return render_template("index.html")


# standard_to = StandardScaler()
@app.route("/predict", methods = ['POST'])
def predict():
    if request.method == 'POST':
        gend = request.form['gender']
        if gend=="Male":
            gd = 1
        else:
            gd = 0
        married = request.form['marry']
        if married == "Yes":
            marr = 1
        else:
            marr=0
        age = int(request.form['age'])
        graduated = request.form['grad']
        if graduated == "Yes":
            grad=1
        else:
            grad=0
        profession = request.form['prof']
        if profession == "Healthcare":
            prof = 5
        elif profession  == "Engineer":
            prof = 2
        elif profession == "Lawyer":
            prof = 7
        elif profession == "Entertainment":
            prof = 3
        elif profession == "Artist":
            prof = 0
        elif profession == "Executive":
            prof = 4
        elif profession == "Doctor":
            prof = 1
        elif profession == "Homemaker":
            prof = 6
        elif profession == "Marketing":    
            prof = 8
        work = int(request.form['work'])
        score_spending = request.form['score']
        if score_spending == "Low":
            score = 0
        elif score_spending == "Average":
            score = 1
        elif score_spending == "High":
            score = 2
        fam_size = int(request.form['fam'])
        var1 = int(request.form['var'])
        prediction = model.predict([[gd,marr,age,grad,prof,work,score,fam_size,var1]])
        return render_template("index.html",results = f"You belong to the customer segment of {prediction}")
    else:
        return render_template("index.html")

    

if __name__ == "__main__":
    app.run(debug=True) 