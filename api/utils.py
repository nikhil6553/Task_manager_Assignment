from datetime import datetime

tasks = []
id_counter = 1

def get_next_id():
    global id_counter
    current_id = id_counter
    id_counter += 1
    return current_id

def find_task(task_id):
    return next((t for t in tasks if t["id"] == task_id), None)

def create_task_object(data):
    return {
        "id": get_next_id(),
        "title": data["title"],
        "description": data.get("description", ""),
        "status": "pending",
        "createdAt": datetime.now().isoformat()
    }