from flask import Flask , render_template, request
from functions import sort_and_filter_reviews, readJson

app = Flask(__name__)

@app.route("/")
def home():
    data = readJson("./reviews.json")
    data = sort_and_filter_reviews(data, request.args)

    return render_template('index.html' , reviews=data)