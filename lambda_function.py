
import json

def lambda_handler(event, context):
    for record in event['Records']:
        print("New file uploaded:")
        print("Bucket:", record['s3']['bucket']['name'])
        print("File:", record['s3']['object']['key'])
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
