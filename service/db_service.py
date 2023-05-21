import boto3


class DbService:

    def __init__(self, dynamodb_client=None):
        if dynamodb_client is None:
            self.dynamodb_client = boto3.client("dynamodb")
        else:
            self.dynamodb_client = dynamodb_client

    def save(self, table_name, item):
        self.dynamodb_client.put_item(
            TableName=table_name,
            Item=item
        )
