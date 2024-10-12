import socket

from julia_sample_scripts.client.gcp.speech_to_text.client import SpeechToTextClient
from julia_sample_scripts.client.gcp.text_to_speech.client import TextToSpeechClient
from julia_sample_scripts.intent_engine.handler import IntentEventHandler
from julia_sample_scripts.julia.player import play_wav
from julia_sample_scripts.stream.stream_buff import StreamBuffer
from julia_sample_scripts.wake_word.wakewordclient import WakeWordClient

# Server settings
SERVER_IP = '192.168.1.30'
SERVER_PORT = 5001
CHUNK = 1024

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print("Waiting for connection...")

conn, addr = server_socket.accept()
print("Connection established with:", addr)
wake_listener = WakeWordClient()
speech_client = TextToSpeechClient()
text_client = SpeechToTextClient()
handler = IntentEventHandler()

with StreamBuffer(conn, CHUNK) as stream:
    awake = False
    while True:
        try:
            while not awake:
                data = conn.recv(CHUNK)
                awake = wake_listener.wake_up(data)
            speech = speech_client.synthesize_speech(f"Hello Dennis.")
            play_wav(speech)
            responses = text_client.transcribe_stream(stream.generator())
            handler.handle(responses)
        except Exception as ex:
            awake = False
