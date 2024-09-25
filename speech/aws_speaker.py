from os import path, remove

import boto3

from speech._base import Speaker

DST_PATH = '/Users/denizulcay/code/local/aws-sample-scripts/resources/speech.mp3'


class AwsSpeaker(Speaker):
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
        with open(DST_PATH, 'wb') as f:
            f.write(response['AudioStream'].read())
