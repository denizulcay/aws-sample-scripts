import string


def clean_text(text: str):
    return text.lower().translate(str.maketrans('', '', string.punctuation))
