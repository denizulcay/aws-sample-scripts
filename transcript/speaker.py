from os import remove, path

import boto3
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream

from transcript.player import play_audio
from transcript.translator import Translator

DST_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.mp3'


class Speaker(object):
    def __init__(self):
        self._client = boto3.Session(region_name='us-west-2').client('polly')
        if path.exists(DST_PATH):
            remove(DST_PATH)

    def text_to_audio(self, text: str):
        response = self._client.synthesize_speech(
            VoiceId='Joanna',
            OutputFormat='mp3',
            Text=text,
            Engine='neural'
        )
        file = open(DST_PATH, 'wb')
        file.write(response['AudioStream'].read())
        file.close()


class SpeakEventHandler(TranscriptResultStreamHandler):
    def __init__(self, transcript_result_stream: TranscriptResultStream):
        super().__init__(transcript_result_stream)
        self._speaker = Speaker()
        self._translator = Translator()
        self._notes_path = "/Users/denizulcay/code/local/aws-sample-scripts/resources/notes/my_notes.txt"

    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        # This handler can be implemented to handle transcriptions as needed.
        # Here's an example to get started.
        results = transcript_event.transcript.results
        for result in results:
            for alt in result.alternatives:
                if not result.is_partial:
                    print(alt.transcript)
                    if alt.transcript in ["Hey, Julia.", "Hey Julia."]:
                        self._speaker.text_to_audio("Hello! How can I help you today?")
                        play_audio(DST_PATH)

                    if alt.transcript in ["Julia.", "Julia", "Julia,"]:
                        self._speaker.text_to_audio("I am listening.")
                        play_audio(DST_PATH)

                    if (alt.transcript.startswith("Hey, Julia, my name is ")
                            or alt.transcript.startswith("Hey Julia, my name is ")):
                        name = alt.transcript.strip("Hey, Julia, my name is ").strip(".").capitalize()
                        self._speaker.text_to_audio(f"Hello {name}! How can I help you today?")
                        play_audio(DST_PATH)

                    if alt.transcript == "Where are my slippers?":
                        self._speaker.text_to_audio("They are under the bed.")
                        play_audio(DST_PATH)

                    if alt.transcript == "Read my notes.":
                        with open(self._notes_path, "r") as file:
                            notes = file.read()
                        self._speaker.text_to_audio(notes)
                        play_audio(DST_PATH)

                    if alt.transcript.startswith("Remind me to "):
                        text = alt.transcript.strip("Remind me to ").capitalize()

                        with open(self._notes_path, "a") as file:
                            file.write("\n")
                            file.write(text)

                        self._speaker.text_to_audio(f"I will remind you to {text}")
                        play_audio(DST_PATH)

                    if alt.transcript == "Clear my notes.":
                        with open(self._notes_path, "w") as file:
                            file.write("")
                        self._speaker.text_to_audio("I cleared your notes for you.")
                        play_audio(DST_PATH)

                    if alt.transcript == "Tell me a joke.":
                        self._speaker.text_to_audio("Why do cows wear bells? Because their horns don't work. Ha Ha Ha.")
                        play_audio(DST_PATH)

                    if alt.transcript == "Power off.":
                        self._speaker.text_to_audio("Goodbye!")
                        play_audio(DST_PATH)
                        raise NotImplementedError()