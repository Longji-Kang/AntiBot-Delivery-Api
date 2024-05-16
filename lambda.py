import boto3
import os

def handler(event, context):
    dynamo = boto3.resource('dynamodb')
    table  = dynamo.Table(os.environ['dynamo_table'])
        
    response = table.query(
        Limit = 1,
        ScanIndexForward = False,
        KeyConditionExpression = "#pk = :pk",
        ExpressionAttributeValues={
              ":pk": 1
        }, 
        ExpressionAttributeNames={
             "#pk":"Id"
        }
    )
    
    item = response['Items']
    
    url = str(item[0]['Url'])
    
    print(url)
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": '{"url": "' + url + '"}'
    }