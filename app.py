from flask import Flask, request

app = Flask(__name__)


@app.route('/video_transform', methods=['GET'])
def video_transform():
    original_video_path = request.args.get('originalVideoPath')
    return f'The original video path is: {original_video_path}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
