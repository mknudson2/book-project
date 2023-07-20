from flask import Flask
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)



#must be at bottom of page to avoid circular import
from app import routes