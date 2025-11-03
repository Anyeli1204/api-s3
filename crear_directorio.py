import boto3

def lambda_handler(event, context):
    # Entrada (json)
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']  # ej: "carpeta/subcarpeta"

    # Asegura el slash final
    if not directorio.endswith('/'):
        directorio += '/'

    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=directorio, Body=b'')

    return {
        'statusCode': 201,
        'bucket': bucket,
        'directorio_creado': directorio
    }
