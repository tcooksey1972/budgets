import boto3

def lambda_handler(event, context):
    # Code to remove SCP from the account
    # Assume a fixed account ID for stub purposes
    account_id = '123456789012'

    client = boto3.client('organizations')
    response = client.detach_policy(
        PolicyId='SCP-policy-id',  # Replace with your SCP policy ID
        TargetId=account_id
    )
    return response
