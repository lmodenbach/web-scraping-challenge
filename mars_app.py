from flask import Flask, render_template
import pymongo
from scrape_mars import scrape

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

scrape_dict = []

@app.route("/")
def home():
    scrape()
    scrape_dict = db.mars.find()
    return render_template("index.html", scraped=scrape_dict)


@app.route("/scrape")
def scrape():
    scrape_dict = scrape()
    db.mars.insert_one(scrape_dict)

if __name__ == "__main__":
    app.run(debug=True)