import boto3

# 1. Connect to AWS S3 service specifically in your Sydney region
s3 = boto3.client('s3', region_name='ap-southeast-2')

# 2. Set your bucket name (Change this to your actual bucket name)
BUCKET_NAME = 'superstore-data-lake-anandh'

print("Connecting to AWS S3...")

try:
    # 3. Ask AWS to list all files inside this specific bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    # 4. Check if the bucket has any files inside it
    if 'Contents' in response:
        print(f"\nSuccessfully connected! Here are the files in '{BUCKET_NAME}':")
        for file in response['Contents']:
            print(f" - {file['Key']}")
    else:
        print(f"\nConnected successfully! However, the bucket '{BUCKET_NAME}' is currently empty.")

except Exception as e:
    print(f"\nAn error occurred while connecting: {e}")
