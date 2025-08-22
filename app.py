from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(message="Hello from Flask on Azure Pipelines!")

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    # Dev server (not for production)
    app.run(host="0.0.0.0", port=5000, debug=True)
