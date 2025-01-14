from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I LOVE NINGNING, I LOVE NINGNING, I LOVE NINGNING, I LOVE NINGNING, I LOVE NINGNING.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
