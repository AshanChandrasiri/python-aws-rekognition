import boto3


class DbService:

    def __init__(self):
        self.dynamodb_client = boto3.client("dynamodb")

    def save(self, table_name, item):
        response = self.dynamodb_client.put_item(
            TableName=table_name,
            Item=item
        )
