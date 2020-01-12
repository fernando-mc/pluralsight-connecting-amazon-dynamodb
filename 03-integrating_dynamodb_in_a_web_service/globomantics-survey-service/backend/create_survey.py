import boto3
import os
import json
import uuid

dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(TABLE_NAME)


def handler(event, context):
    survey_data = json.loads(event['body'])
    survey_id = str(uuid.uuid4())
    survey_data['survey_id'] = survey_id
    result = table.put_item(
        Item=survey_data
    )
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin":"*"},
        "body": json.dumps({"survey_id" : survey_id})
    }
    return response