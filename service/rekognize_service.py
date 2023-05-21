import boto3


class RekognizeService:

    def __init__(self, rek_client=None):
        if rek_client is None:
            self.rek_client = boto3.client('rekognition')
        else:
            self.rek_client = rek_client

    def detect_labels(self, image_bytes):
        response = self.rek_client.detect_labels(Image={'Bytes': image_bytes})
        return response
