from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from celery import Celery

app=Flask(__name__)
app.config.from_object('project.config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
cache = Cache(app)

celery = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)
