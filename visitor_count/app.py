import json
import simplejson
from decimal import Decimal
import boto3

# import requests


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('statistics')
    response = table.update_item(
        Key={
            'page': 'home'
        },
        UpdateExpression="ADD visitcount :num",
        ExpressionAttributeValues={
            ':num': Decimal(1)
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": simplejson.dumps(response),
    }
