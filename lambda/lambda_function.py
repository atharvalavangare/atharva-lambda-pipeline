def lambda_handler(event, context):
    print("Lambda triggered!")
    print("Event:", event)
    return {
        'statusCode': 200,
        'body': 'Success'
    }