from flask import Flask, render_template, request, redirect
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    try:
        raise Exception("Testing")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("Testing 2")
    return "<h1>CI/CD pipeline has established</h1>"

if __name__=="__main__":
    app.run(debug=True)
    