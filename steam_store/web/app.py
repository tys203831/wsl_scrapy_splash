from flask import Flask
from flask.templating import render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    resp = requests.get(url="http://localhost:9080/crawl.json?start_requests=true&spider_name=best_selling").json()
    items = json.dumps(resp.get("items"))
    return items

@app.route("/show")
def show_template():
    resp = requests.get(url="http://localhost:9080/crawl.json?start_requests=true&spider_name=best_selling").json()
    items = resp.get("items")
    return render_template("index.html", games = items)

if __name__ == "__main__":
    app.run(debug=True)
