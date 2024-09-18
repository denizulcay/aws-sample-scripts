import webbrowser
from os import remove, path, system

import boto3
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream

from joker.joker import Joker
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
        self._joker = Joker()
        self._notes_path = "/Users/denizulcay/code/local/aws-sample-scripts/resources/notes/my_notes.txt"
        self._person = None

    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        results = transcript_event.transcript.results
        for result in results:
            for alt in result.alternatives:
                if not result.is_partial:
                    print(alt.transcript)
                    if alt.transcript in ["Hey, Julia.", "Hey Julia."]:
                        self._speaker.text_to_audio("Hello! How can I help you today?")
                        play_audio(DST_PATH)

                    elif alt.transcript in ["Julia.", "Julia", "Julia,"]:
                        self._speaker.text_to_audio("I'm listening.")
                        play_audio(DST_PATH)

                    elif alt.transcript.startswith("My name is "):
                        name = alt.transcript.replace("My name is ", "").strip(".").capitalize()
                        self._person = name
                        self._speaker.text_to_audio(f"Hello {self._person}! How can I help you today?")
                        play_audio(DST_PATH)

                    elif alt.transcript == "Launch Chrome browser.":
                        self._speaker.text_to_audio("Launching Chrome Browser.")
                        play_audio(DST_PATH)
                        system("open /Applications/Google\ Chrome.app")

                    elif alt.transcript in "Kill Chrome browser.":
                        self._speaker.text_to_audio("Killing Chrome Browser.")
                        play_audio(DST_PATH)
                        system("osascript -e 'quit app \"Google Chrome\"'")

                    elif alt.transcript == "Launch my workspace.":
                        self._speaker.text_to_audio("Launching your workspace.")
                        play_audio(DST_PATH)
                        (webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("https://myworkspace.jpmchase.com"))

                    elif alt.transcript == "Where are my slippers?":
                        self._speaker.text_to_audio("They are under the bed.")
                        play_audio(DST_PATH)

                    elif alt.transcript == "Read my notes.":
                        with open(self._notes_path, "r") as file:
                            notes = file.read()
                        self._speaker.text_to_audio(notes)
                        play_audio(DST_PATH)

                    elif alt.transcript.startswith("Remind me to "):
                        text = alt.transcript.replace("Remind me to ", "").replace("my", "your").capitalize()

                        with open(self._notes_path, "a") as file:
                            file.write(f"{text}\n")

                        self._speaker.text_to_audio(f"I will remind you to {text}")
                        play_audio(DST_PATH)

                    elif alt.transcript == "Clear my notes.":
                        remove(self._notes_path)
                        self._speaker.text_to_audio("I cleared your notes for you.")
                        play_audio(DST_PATH)

                    elif alt.transcript == "Tell me a joke.":
                        joke = self._joker.tell_joke()
                        self._speaker.text_to_audio(f"{joke} Ha Ha Ha.")
                        play_audio(DST_PATH)

                    elif alt.transcript == "Power off.":
                        if self._person:
                            self._speaker.text_to_audio(f"Goodbye {self._person}!")
                        else:
                            self._speaker.text_to_audio(f"Goodbye!")
                        play_audio(DST_PATH)
                        raise NotImplementedError()

                    # else:
                    #     self._speaker.text_to_audio(
                    #         "I don't have all the answers. I'm just a computer program you know..."
                    #     )
                    #     play_audio(DST_PATH)
