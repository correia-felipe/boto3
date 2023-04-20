from datetime import date,timedelta
import boto3
import json

data = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
#creating boto3 client using self credentials
s3 = boto3.client('s3',
                   aws_access_key_id="Access key ID",
                   aws_secret_access_key= "Secret access key"
                  )
#bucket data - s3 endpoint
bucket_name = "bucket name"
object_name = f'"prefix"/{data}_"nome do arquivo".json'

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