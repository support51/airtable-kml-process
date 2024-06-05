from flask import Flask, render_template
from airtableKmlProcess import process_airtable_and_kml
app = Flask(__name__)

def test():
    print("Hello world")

@app.route("/", methods = ["GET","POST"])
def home():
    return render_template("helloworld.html")

@app.route("/kml", methods = ["GET","POST"])
def home():
    process_airtable_and_kml()
    print(200)
    return render_template("helloworld.html")