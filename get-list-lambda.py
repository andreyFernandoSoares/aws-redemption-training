import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    userId = event['pathParameters']['userid']
    table = client.Table("movie")
    response = table.get_item(TableName="movie", Key={'userId': userId})
    return {
        "status": 200,
        "mensagem": response
    }
