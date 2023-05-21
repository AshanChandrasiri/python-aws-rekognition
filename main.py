import argparse
import os
from service.db_service import DbService
from service.image_processor_service import ImageProcessorService
from service.rekognize_service import RekognizeService


def parse_args():
    parser = argparse.ArgumentParser(description='argument for app')
    parser.add_argument('url', help='image url is required')
    parser.add_argument('extension', help='image extension')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print(args.url)
    rekognize_service = RekognizeService()
    db_service = DbService()
    image_processor_service = ImageProcessorService(rekognize_service, db_service)
    image_processor_service.process(args.url, args.extension)
