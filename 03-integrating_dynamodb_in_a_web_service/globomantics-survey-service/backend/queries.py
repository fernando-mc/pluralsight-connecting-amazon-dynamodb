import boto3
import uuid

from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table('gss')

def create_customer_profile(customer_id, profile_data):
    item = {
        'pk': 'CUSTOMER#' + customer_id,
        'sk': 'PROFILE#' + customer_id,
        'profile_data': profile_data
    }
    table.put_item(Item=item)
    return item


def get_customer_profile(customer_id):
    response = table.get_item(
        Key={
            'pk': 'CUSTOMER#' + customer_id,
            'sk': 'PROFILE#' + customer_id
        }
    )
    return response['Item']


def create_customer_survey(customer_id):
    survey_id = str(uuid.uuid4())


// Create or get a specific customer survey:
pk = CUSTOMER#custumerId AND sk = SURVEY#surveyId

// Get all customer surveys:
pk = CUSTOMER#customerId AND sk BEGINS_WITH “SURVEY#”

// Create or get a single survey response: 
pk = RESPONSE#responseId AND sk = SURVEY#surveyId



INDEX:
// Get all responses to a survey: 
pk = SURVEY#surveyId AND sk BEGINS_WITH “RESPONSE#”
// Get a specific survey by id:
pk = SURVEY#surveyId AND sk BEGINS_WITH “CUSTOMER#”
