#!/usr/bin/env python
import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello here"


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', False))
