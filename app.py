from flask import Flask, jsonify, g

from flask_cors import CORS

from flask_login import LoginManager

import models

# importing resource
# from resources.countdowns import countdowns
# from resources.users import users


DEBUG = True
PORT = 8000


app = Flask(__name__)

app.secret_key = "jurgendavid"

# CORS(countdowns, origins=["http://localhost:3000"], supports_credentials=True)
# CORS(users, origins=["http://localhost:3000"], supports_credentials=True)

# app.register_blueprint(countdowns, url_prefix="/api/v1/countdowns")
# app.register_blueprint(users, url_prefix="/api/v1/users")


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/')
def index():
    return 'Hello, world!'


if __name__ == "__main__":
    print("tables connected")
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
