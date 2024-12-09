from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Vishal! Welcome to the Flask App.'

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    # Returning a JSON response for better clarity
    return jsonify(status="UP", message="Flask app is running"), 200

if __name__ == '__main__':
    # Ensures the app is accessible outside the container
    app.run(host='0.0.0.0', port=5000)
