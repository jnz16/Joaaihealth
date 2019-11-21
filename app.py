#These modules are from flask
from flask import Flask, render_template, request
#This module is from dotenv
from dotenv import load_dotenv
#These are python provided modules
import requests, os

app= Flask("BreastApp")

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/userreport", methods=["GET", "POST"])
def user_name():
    form_data = request.form
    name=form_data["name"]
    symptoms = form_data.getlist("checkbox")
    print(symptoms)

    if ("swollen" in symptoms) or ("lump" in symptoms) or ("nipple" in symptoms):
        return render_template("referGP.html", symptomresult = symptoms, user_data=form_data)
    if ("dimpling" in symptoms) or ("pain" in symptoms):
        return render_template("wait48h.html", symptomresult=symptoms, user_data=form_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

app.run(debug=True)