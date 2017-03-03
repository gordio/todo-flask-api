#!/usr/bin/env python
import os
from flask import Flask


app = Flask(__name__)


tasks = [{
    'id': 1,
    'title': "Task 1",
    'done': False
}, {
    'id': 2,
    'title': "Task 2",
    'done': False
}]


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', False))
