from flask import Flask, render_template
import pymongo

app = Flask(__name__)


@app.route("/scrape")
def scrape():
    

if __name__ == "__main__":
    app.run(debug=True)