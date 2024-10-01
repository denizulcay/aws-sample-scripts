from julia_sample_scripts.camera.photo import take_picture
from julia_sample_scripts.client.aws.rekognition.client import RekognitionClient


def recognize_user():
    face_client = RekognitionClient()
    user = face_client.search_name_by_image(image=take_picture())

    return user


def add_user(name: str):
    face_client = RekognitionClient()
    face_client.index_face(image=take_picture(), name=name)
