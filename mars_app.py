from flask import Flask, render_template
import pymongo
from scrape_mars_d1 import scrape

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

data_from_mongo = {}
mars_data_dict = {}

@app.route("/")
def home():
    function_call()
    data_from_mongo = db.mars.find_one()
    print(data_from_mongo)
    return render_template("index.html", scraped=data_from_mongo)


@app.route("/scrape")
def function_call():
    mars_data_dict = scrape()
    db.mars.insert_one(mars_data_dict)

if __name__ == "__main__":
    app.run(debug=True)