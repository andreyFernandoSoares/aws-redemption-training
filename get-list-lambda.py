import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = client.Table("movie")
    response = table.scan()

    return {
        "status": 200,
        "mensagem": response['Items']
    }
