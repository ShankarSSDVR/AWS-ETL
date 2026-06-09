import boto3

# Create S3 client
s3 = boto3.client(
    's3',
    region_name='ap-southeast-2'
)

# Your bucket name
bucket_name = 'etl-data-lake-anandh'
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'
    }
)
# Local file path on your laptop
local_file = r'D:\Study\Data for data enginnering practice\data\USvideos.csv'

# S3 path (raw layer)
s3_key = 'raw/USvideos.csv'

try:
    s3.upload_file(local_file, bucket_name, s3_key)
    print(f"File uploaded successfully to s3://{bucket_name}/{s3_key}")

except Exception as e:
    print("Error:", e)