from flask import Flask, render_template, request
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/visit")
def visit():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get("http://127.0.0.1:8000")
        try:
            driver.get(request.args.get("site"))
            driver.add_cookie({"name": "favorite_site", "value": "blahaj{x55_exi5t5_n0t_ju5t_in_scr1pt}"})
            driver.refresh()
            return "Visited"
        except:
            return "Invalid URL"


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
