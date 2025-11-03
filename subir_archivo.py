import base64
import boto3
import mimetypes

def lambda_handler(event, context):
    bucket = event['body']['bucket']     # ej: "mi-bucket"
    key = event['body']['key']           # ej: "imagenes/foto.png" o "src/main.cpp"
    data_b64 = event['body']['base64']   # base64 del archivo

    # Detecta content-type si viene como data URI
    content_type = None
    if data_b64.startswith('data:'):
        header, data_b64 = data_b64.split(',', 1)
        # data:image/png;base64,....
        semi = header.find(';')
        content_type = header[5:semi] if semi != -1 else header[5:]

    # Si no hay content-type aún, intenta por extensión del key
    if not content_type:
        guessed, _ = mimetypes.guess_type(key)
        content_type = guessed or 'application/octet-stream'

    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=base64.b64decode(data_b64),
        ContentType=content_type
    )

    return {
        'statusCode': 201,
        'bucket': bucket,
        'key': key,
        'ruta': f's3://{bucket}/{key}',
        'contentType': content_type
    }
