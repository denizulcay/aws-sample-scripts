import boto3


class Translator:
    def __init__(self):
        self._client = boto3.Session(region_name='us-east-2').client('translate')

    def translate(self, text):
        return self._client.translate_text(
            Text=text,
            SourceLanguageCode='en',
            TargetLanguageCode='tr'
        )['TranslatedText']
