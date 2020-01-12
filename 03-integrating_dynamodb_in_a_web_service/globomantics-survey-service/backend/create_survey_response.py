import boto3
import os
import json
import uuid

dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(TABLE_NAME)


def handler(event, context):
    response_data = json.loads(event['body'])
    response_id = str(uuid.uuid4())
    response_data['response_id'] = response_id
    print(event)
    result = table.put_item(
        Item=response_data
    )
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin":"*"},
        "body": json.dumps({"response_id" : response_id})
    }
    return response