
from speech.aws_speaker import AwsSpeaker
from util.text import clean_text
from intent_engine._const import _CLASSIFY_MAP


class IntentEngine:
    _speaker = AwsSpeaker()
    _notes_path = "/Users/denizulcay/code/local/aws-sample-scripts/resources/notes/my_notes.txt"
    _person = None

    @classmethod
    def resolve(cls, text: str):
        for key, value in _CLASSIFY_MAP.items():
            if value(text):
                return key
        # if text == "hey julia":
        #     cls._speaker.text_to_audio("Hello! How can I help you today?")
        #     play_audio(DST_PATH)
        #
        # elif text == "julia":
        #     cls._speaker.text_to_audio("I'm listening.")
        #     play_audio(DST_PATH)
        #
        # elif text.startswith("my name is "):
        #     name = text.replace("My name is ", "").strip(".").capitalize()
        #     cls._person = name
        #     cls._speaker.text_to_audio(f"Hello {cls._person}! How can I help you today?")
        #     play_audio(DST_PATH)
        #
        # elif text == "launch chrome browser":
        #     cls._speaker.text_to_audio("Launching Chrome Browser.")
        #     play_audio(DST_PATH)
        #     system("open /Applications/Google\ Chrome.app")
        #
        # elif text in "kill chrome browser":
        #     cls._speaker.text_to_audio("Killing Chrome Browser.")
        #     play_audio(DST_PATH)
        #     system("osascript -e 'quit app \"Google Chrome\"'")
        #
        # elif text == "launch my workspace":
        #     cls._speaker.text_to_audio("Launching your workspace.")
        #     play_audio(DST_PATH)
        #     (webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("https://myworkspace.jpmchase.com"))
        #
        # elif text == "where are my slippers":
        #     cls._speaker.text_to_audio("They are under the bed.")
        #     play_audio(DST_PATH)
        #
        # elif text == "read my notes":
        #     with open(cls._notes_path, "r") as file:
        #         notes = file.read()
        #     cls._speaker.text_to_audio(notes)
        #     play_audio(DST_PATH)
        #
        # elif text.startswith("remind me to "):
        #     text = text.replace("remind me to ", "").replace("my", "your").capitalize()
        #
        #     with open(cls._notes_path, "a") as file:
        #         file.write(f"{text}\n")
        #
        #     cls._speaker.text_to_audio(f"I will remind you to {text}")
        #     play_audio(DST_PATH)
        #
        # elif text == "clear my notes":
        #     remove(cls._notes_path)
        #     cls._speaker.text_to_audio("I cleared your notes for you.")
        #     play_audio(DST_PATH)
        #
        # elif text == "tell me a joke":
        #     joke = cls._joker.tell_joke()
        #     cls._speaker.text_to_audio(f"{joke} Ha Ha Ha.")
        #     play_audio(DST_PATH)
        #
        # elif text == "power off":
        #     if cls._person:
        #         cls._speaker.text_to_audio(f"Goodbye {cls._person}!")
        #     else:
        #         cls._speaker.text_to_audio(f"Goodbye!")
        #     play_audio(DST_PATH)
        #     raise NotImplementedError()

        # else:
        #     cls._speaker.text_to_audio(
        #         "I don't have all the answers. I'm just a computer program you know..."
        #     )
        #     play_audio(DST_PATH)

