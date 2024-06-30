from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/video_transform')
def video_transform():
    return 'video_transform'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
