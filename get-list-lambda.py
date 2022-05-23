import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = client.Table("movie")
    response = table.scan()
    data = response['Items']
    return {
        "status": 200,
        "mensagem": data
    }
