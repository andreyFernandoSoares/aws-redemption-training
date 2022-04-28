import boto3
import uuid

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    movieId = uuid.uuid4().hex
    event['movieId'] = movieId
    
    table = client.Table("movie")
    table.put_item(Item=event)
    
    return {
        "status": 201,
        "mensagem": "Filme criado com sucesso"
    }
