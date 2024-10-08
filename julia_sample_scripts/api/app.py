from flask import Flask, Response, request

from julia_sample_scripts.wake_word.listener import Listener

app = Flask(__name__)

def yielder():
    with open('/Users/denizulcay/code/local/aws-sample-scripts/resources/wake_word/hello.wav', 'rb') as f:
        yield f.read()

@app.route('/hello')
def hello():
    return Response(yielder(), mimetype='audio/wav')


@app.route('/request', methods=['POST'])
def request_api():
    wake_listener = Listener()
    data = request.data
    num_frames = len(data) // 1024
    for i in range(num_frames):
        awake = wake_listener.wake_up(data[i * 1024:i * 1024 + 1024])
        print(awake)
        if awake:
            return Response(yielder(), mimetype='audio/wav')
    return Response()
