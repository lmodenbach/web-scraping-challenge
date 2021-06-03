from flask import Flask, render_template
import pymongo
from scrape_mars import scrape

app = Flask(__name__)

scrape_dict = []

@app.route("/")
def home():
    return render_template("index.html", scraped=scrape_dict)


@app.route("/scrape")
def scrape():
    scrape_dict = scrape()

if __name__ == "__main__":
    app.run(debug=True)