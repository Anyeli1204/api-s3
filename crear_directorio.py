import boto3

def lambda_handler(event, context):
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']  
    if not directorio.endswith('/'):
        directorio += '/'

    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=directorio, Body=b'')

    return {
        'statusCode': 201,
        'bucket': bucket,
        'directorio_creado': directorio
    }
