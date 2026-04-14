from flask import Blueprint, request, jsonify
from api.utils import tasks, find_task, create_task_object

task_bp = Blueprint('tasks', __name__)

# POST /tasks
@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"message": "Title is required"}), 400

    task = create_task_object(data)
    tasks.append(task)

    return jsonify(task), 201


# GET /tasks
@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    result = tasks.copy()

    status = request.args.get('status')
    sort = request.args.get('sort')

    #Filter by status
    if status:
        if status not in ['pending', 'done']:
            return jsonify({"message": "Invalid status value"}), 400
        result = [t for t in result if t["status"] == status]

    #Sort by createdAt
    if sort:
        if sort != "createdAt":
            return jsonify({"message": "Invalid sort field"}), 400
        result.sort(key=lambda x: x["createdAt"])

    return jsonify(result)


# GET /tasks/<id>
@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    return jsonify(task)


# PUT /tasks/<id>
@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = find_task(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json()

    if not data or ("title" not in data and "description" not in data):
        return jsonify({"message": "Nothing to update"}), 400

    if "title" in data:
        task["title"] = data["title"]

    if "description" in data:
        task["description"] = data["description"]

    return jsonify(task)


# PATCH /tasks/<id>/done
@task_bp.route('/tasks/<int:task_id>/done', methods=['PATCH'])
def mark_done(task_id):
    task = find_task(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    task["status"] = "done"
    return jsonify(task)


# DELETE /tasks/<id>
@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    tasks.remove(task)
    return jsonify({"message": "Task deleted successfully"})


# 405 Handler
@task_bp.app_errorhandler(405)
def method_not_allowed(e):
    return jsonify({"message": "Method Not Allowed"}), 405