import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = client.Table("movies")
    response = table.scan()
    items = response['Items']
    print(items)
    return {
        'statusCode': 200,
        'body': items
    }
