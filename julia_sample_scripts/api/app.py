
from flask import Flask, Response, request

from julia_sample_scripts.julia.handler import JuliaHandler

app = Flask(__name__)

FRAME_LENGTH = 512
INT16_SIZE = 2
CHUNK_SIZE = FRAME_LENGTH * INT16_SIZE


@app.route('/wake', methods=['POST'])
def wake_api():
    handler = JuliaHandler()
    result = handler.handle_wake(request.data)
    if result:
        response = Response(result, mimetype='audio/wav', status=200)
    else:
        response = Response(status=204)

    return response


@app.route('/request', methods=['POST'])
def request_api():
    handler = JuliaHandler()
    result = handler.handle_transcript(request.data)
    if result:
        response = Response(result, mimetype='audio/wav', status=200)
    else:
        response = Response(status=204)

    return response
