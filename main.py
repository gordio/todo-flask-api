#!/usr/bin/env python
import os
from flask import Flask, jsonity, make_response


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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/v1.0/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', False))
