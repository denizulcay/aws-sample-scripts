from typing import Any

import boto3
from boto3.dynamodb.conditions import Key

DYNAMODB: str = "dynamodb"


class DynamoDbClient:
    def __init__(self, region):
        self._region = region
        self._client = boto3.resource(DYNAMODB, region_name=self._region)

    def get_row(self, table_name: str, key_col: str, key: str) -> Any:
        table = self._client.Table(table_name)
        result = table.query(KeyConditionExpression=Key(key_col).eq(key))["Items"][0]

        return result

    def get_value(self, table_name: str, key_col: str, key: str, value_column: str) -> Any:
        return self.get_row(table_name=table_name, key_col=key_col, key=key)[value_column]
