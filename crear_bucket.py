import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']

    s3 = boto3.client('s3')
    region = s3.meta.region_name or 'us-east-1'
    params = {'Bucket': nombre_bucket}
    if region != 'us-east-1':
        params['CreateBucketConfiguration'] = {'LocationConstraint': region}

    s3.create_bucket(**params)

    return {
        'statusCode': 201,
        'bucket': nombre_bucket,
        'region': region
    }
