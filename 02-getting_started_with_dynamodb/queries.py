import boto3
from boto3.dynamodb.conditions import Key

tablename = "basicSongsTable"
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(tablename)

# Get all songs by artist
response = table.query(KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian'))
print(response['Items'])

# List all songs by an artist that start with a certain name
response = table.query(KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian') & Key('song').begins_with('Carrot'))
print(response['Items'])