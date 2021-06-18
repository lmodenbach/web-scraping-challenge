#necessary imports

from flask import Flask, render_template
import pymongo
from scrape_mars import scrape

app = Flask(__name__)

#connect to mongodb using pymongo, connect mars_db in mongodb to a variable

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

#create dictionaries - one for the scrape function return, one for the database call return 

data_from_mongo = {}
mars_data_dict = {}

#populate home page with call to scrape followed by call to database, then pass data to template

@app.route("/")
def home():
    function_call()
    data_from_mongo = db.mars.find_one()
    return render_template("index.html", scraped=data_from_mongo)

#scrape route/function calls scrape script, drops the mars collection from mars_db and recreates/ 
#repopulates it with a new entry

@app.route("/scrape")
def function_call():
    mars_data_dict = scrape()
    db.mars.drop()
    db.mars.insert_one(mars_data_dict)

if __name__ == "__main__":
    app.run(debug=True)