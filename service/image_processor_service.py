import requests
import uuid
import os
from PIL import Image

from service.db_service import DbService
from service.rekognize_service import RekognizeService

DOWNLOAD_PATH = '{}.{}'


class ImageProcessorService:

    def __init__(self, rekognize_service: RekognizeService, db_service: DbService):
        self.rekognize_service = rekognize_service
        self.db_service = db_service

    def process(self, image_url, extension='jpg'):
        image_path = self.download_image(image_url, extension)
        with open(image_path, 'rb') as image:
            response = self.rekognize_service.detect_labels(image.read())

            labels: list = response['Labels']
            if len(labels) == 0:
                print(f'No labels found for image {image_url}')
                return

            labels.sort(key=lambda item: item['Confidence'], reverse=True)
            result = []
            for label in labels[0:5]:
                name = label['Name']
                confidence = label['Confidence']
                print(f'confidence {confidence} - name {name}')
                result.append({
                    'label': name,
                    'confidence': confidence
                })
                self.save(name, image_url, confidence)

        self.delete_image(image_path)
        print(f'successfully processed {len(result)} labels. {result}')

    def download_image(self, image_url, extension='jpg'):
        path = DOWNLOAD_PATH.format(str(uuid.uuid1()), extension)
        img = Image.open(requests.get(image_url, stream=True).raw)
        img.save(path)
        return path

    def save(self, name, url, confidence):
        record = {
            'name': {'S': name},
            'url': {'S': url},
            'confidence': {'S': str(round(confidence, 2))}
        }
        self.db_service.save('image-process-result', record)

    def delete_image(self, image_path):
        os.remove(image_path)
