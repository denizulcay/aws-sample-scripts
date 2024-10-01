import boto3

COLLECTION = "app-julia-authorized-users"


class RekognitionClient:
    def __init__(self):
        self._client = boto3.Session(region_name='us-east-2').client('rekognition')

    def search_name_by_image(self, image: bytes) -> str:
        response = self._client.search_faces_by_image(
            CollectionId="app-julia-authorized-users",
            Image={"Bytes": image},
            FaceMatchThreshold=80,
            MaxFaces=1,
        )
        name = response['FaceMatches'][0]['Face']['ExternalImageId'] if response['FaceMatches'] else None

        return name

    def index_face(self, image: bytes, name: str, collection_id=COLLECTION):
        self._client.index_faces(
            CollectionId=collection_id,
            Image={"Bytes": image},
            ExternalImageId=name,
            MaxFaces=1,
            DetectionAttributes=["ALL"],
        )

# client = RekognitionClient()
# client._client.delete_collection(CollectionId="app-julia-authorized-users")
# client._client.create_collection(CollectionId="app-julia-authorized-users")

