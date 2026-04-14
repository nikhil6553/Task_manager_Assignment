from flask import Flask
from api.routes import task_bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(task_bp)

@app.route('/')
def home():
    return "Task Manager is Running!"

if __name__ == '__main__':
    app.run(debug=True)