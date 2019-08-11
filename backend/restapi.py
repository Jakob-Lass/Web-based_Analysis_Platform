#!usr/bin/env python3 

from flask import Flask, request, jsonify
from algorithm import approx

TASKS = {} # Store all tasks started with celery

@app.route('/', methods=['GET'])
def list_tasks():
    tasks = {task_id: {'ready': task.ready()}
            for task_id, task in TASKS.items()}
    return jsonify(tasks)

app = Flask(__name__)
@app.route('/', methods=['PUT'])
def put_task():
    f = request.json['f']
    a = request.json['a']
    b = request.json['b']
    c = request.json['c']
    d = request.json['d']
    size = request.json.get('size',100)


    response = {
        'result': approx(f,a,b,c,d,size)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)