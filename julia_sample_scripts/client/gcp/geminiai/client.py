import google.generativeai as genai


class GeminiAiClient:
    def __init__(self):
        genai.configure(api_key='AIzaSyBgu15zg-ZcISvgQaSiG1J3iiDRmtwiWug')
        self._model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_content(self, prompt):
        response = self._model.generate_content(prompt)

        return response.text
