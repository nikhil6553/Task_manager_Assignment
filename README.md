## Task Manager REST API (Flask)

A simple REST API built using Flask to manage tasks. Users can create, update, mark tasks as completed, and delete them. The data is stored in memory (no database required).

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd task-manager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## API Endpoints

### 1. Create Task

* **Method:** POST
* **URL:** `/tasks`

**Request Body (JSON):**

```json
{
  "title": "Study AI",
  "description": "Finish assignment"
}
```

**Response:**

* 201 Created

---

### 2. Get All Tasks

* **Method:** GET
* **URL:** `/tasks`

**Response:**

* 200 OK

---

### 3. Get Task by ID

* **Method:** GET
* **URL:** `/tasks/{id}`

**Example:**

```
/tasks/1
```

**Response:**

* 200 OK
* 404 Not Found (if task does not exist)

---

### 4. Update Task

* **Method:** PUT
* **URL:** `/tasks/{id}`

**Request Body:**

```json
{
  "title": "Updated Task"
}
```

**Response:**

* 200 OK
* 400 Bad Request
* 404 Not Found

---

### 5. Mark Task as Done

* **Method:** PATCH
* **URL:** `/tasks/{id}/done`

**Response:**

* 200 OK
* 404 Not Found

---

### 6. Delete Task

* **Method:** DELETE
* **URL:** `/tasks/{id}`

**Response:**

* 200 OK
* 404 Not Found

---

## Testing

The API was tested using **Postman**.

Steps:

1. Open Postman
2. Create requests for each endpoint
3. Use JSON body for POST and PUT requests
4. Verify status codes and responses

---

## Project Structure

```
task-manager/
│
├── app.py
├── api/
│   ├── __init__.py
│   ├── routes.py
│   └── utils.py
│
└── requirements.txt
```

---

## Notes

* Data is stored in memory (will reset when server restarts)
* Designed for simplicity and clarity
* Follows REST API best practices
