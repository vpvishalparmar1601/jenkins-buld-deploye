from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'both pipeline is work properlly pipeline buls and deploye '

if __name__ == '__main__':
    # Ensures the app is accessible outside the container
    app.run(host='0.0.0.0', port=5000)
