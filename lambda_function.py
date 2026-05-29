import json
import boto3
import urllib.parse

sns = boto3.client('sns')

TOPIC_ARN = 'arn:aws:sns:ap-south-1:031871827993:file-upload-alerts'

def lambda_handler(event, context):

    print("Event:", event)

    for record in event['Records']:

        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(
            record['s3']['object']['key']
        )

        message = f"""
New file uploaded!

Bucket: {bucket}
File: {key}
"""

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject='S3 File Upload Alert',
            Message=message
        )

        print("SNS notification sent")

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }