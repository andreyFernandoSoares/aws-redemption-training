import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = client.Table("movies")
    table.put_item(Item=event)
    return {
        "status": 201,
        "mensagem": "Filme criado com sucesso"
    }
