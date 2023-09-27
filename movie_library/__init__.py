import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import redis
from rq import Queue

from movie_library.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)

    connection = redis.from_url(os.getenv("REDIS_URL"))
    app.queue = Queue("emails", connection=connection)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "Alex")
    client = MongoClient(app.config["MONGODB_URI"])
    app.db = client["Alexander23"]
    app.register_blueprint(pages)
    return app
