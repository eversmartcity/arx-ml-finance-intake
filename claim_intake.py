from flask import Flask, request, jsonify
from tasks import process_claim

app = Flask(__name__)

@app.route("/submit-claim", methods=["POST"])
def submit_claim():
    data = request.get_json()
    result = process_claim.delay(data)
    return jsonify({"task_id": result.id, "status": "processing"}), 202

if __name__ == "__main__":
    app.run(debug=True)
