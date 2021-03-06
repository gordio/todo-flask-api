#!/usr/bin/env python
import os
from flask import Flask, abort, request, jsonify, make_response


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


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/v1.0/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})


@app.route('/api/v1.0/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [t for t in tasks if t['id'] == task_id]
    if len(task) == 0 or not request.json or not 'title' in request.json:
        abort(400)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not "title" in request.json:
        abort(400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False,
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', False))
