import boto3
import json

def lambda_handler(event, context):
    # Extract account ID from the SNS message
    # message = json.loads(event['Records'][0]['Sns']['Message'])
    # account_id = message['account']

    # Assume this is the account ID for stub purposes
    account_id = '123456789012'

    # Code to attach SCP to the account
    # Use boto3 to interact with AWS Organizations
    client = boto3.client('organizations')
    response = client.attach_policy(
        PolicyId='SCP-policy-id',  # Replace with your SCP policy ID
        TargetId=account_id
    )
    return response
