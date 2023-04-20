from datetime import date,timedelta
import boto3
import json

data = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
#creating boto3 client using self credentials
s3 = boto3.client('s3',
                   aws_access_key_id='XXXXXXXXXXXXXXXXXXX',
                   aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                  )
#bucket data - s3 endpoint
bucket_name = 'XXXXXXXXXXXXXXXXXXXXXXXX'
object_name = f'XXXXXXXXXXXXX/{data}_XXXXXXXXXXX.json'

#get obj
response = s3.get_object(Bucket=bucket_name, Key=object_name)
#read json
json_data = response['Body'].read()
#decoding json
json_content = json.loads(json_data)
#write locally
with open('XXXXXXXXXXXXXXXXXXXXX.json', 'w') as f:
    json.dump(json_content, f)

json_content