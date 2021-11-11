import os
from flask import Flask


posts = article_list.posts

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world"

app.run()
