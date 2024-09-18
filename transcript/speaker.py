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
            # VoiceId='',
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

    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        # This handler can be implemented to handle transcriptions as needed.
        # Here's an example to get started.
        results = transcript_event.transcript.results
        for result in results:
            for alt in result.alternatives:
                if not result.is_partial:
                    # text = self._translator.translate(alt.transcript)
                    self._speaker.text_to_audio(alt.transcript)
                    play_audio(DST_PATH)
