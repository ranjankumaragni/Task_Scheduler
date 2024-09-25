from flask import Flask, request, jsonify
from task_scheduler import add_task

app = Flask(__name__)

# Route to submit a new task
@app.route('/submit_task', methods=['POST'])
def submit_task():
    task_data = request.json.get('task')
    if task_data:
        add_task(task_data)
        return jsonify({"message": f"Task '{task_data}' added to queue"}), 200
    return jsonify({"error": "No task provided"}), 400

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Running"}), 200

if __name__ == '__main__':
    app.run(debug=True)
