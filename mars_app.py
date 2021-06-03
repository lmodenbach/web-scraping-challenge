from flask import Flask, render_template
import pymongo
import scrape_mars

app = Flask(__name__)

scrape_dict = []

@app.route("/")
def home():
    return render_template("index.html", scraped=scrape_dict)


@app.route("/scrape")
def scrape():
    scrape_dict = scrape_mars.scrape()

if __name__ == "__main__":
    app.run(debug=True)