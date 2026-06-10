import boto3
import pandas as pd
from io import StringIO

bucket_name = "etl-data-lake-anandh"

def create_bi_data():

    s3 = boto3.client('s3', region_name='ap-southeast-2')

    # Read cleaned file from S3
    obj = s3.get_object(
        Bucket=bucket_name,
        Key='devdata/USvideos_clean.csv'
    )

    df = pd.read_csv(obj['Body'])

    # Example transformation:
    # Convert all column names to lowercase

    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    # Save back to S3 under bi_data folder

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3.put_object(
        Bucket=bucket_name,
        Key='devdata/USvideos_bi.csv',
        Body=csv_buffer.getvalue()
    )

    print("BI data created successfully")

if __name__ == "__main__":
    create_bi_data()