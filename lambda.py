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
    
    if len(item) > 0:
        url = str(item[0]['Url'])
        
        print(url)
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": '{"url": "' + url + '"}'
        }
    
    else:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": '{"url": "NaN"}'
        }