import boto3

s3 = boto3.resource('s3')
bucket_name = "kmm-crud-demo-1-2024"

all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
#iterate through all buckets in account and assigm them to the list named all_my_buckets
#create bucket if it does not exist. If already created, use else statement.
if bucket_name not in all_my_buckets:
    print(f"'{bucket_name}' bucket does not exist. Creating now...")
    s3.create_bucket(Bucket=bucket_name)
    print(f"'{bucket_name}' bucket has been created.")
else:
    print(f"'{bucket_name}' bucket already exists. No need to create a new one.")

#CREATE files and make variables for them. 
file_a = 'file_a.txt'
file_b = 'file_b.txt'
# UPLOAD 'file_a' to the new bucket 
#then check is s3 to see if file is in our bucket
s3.Bucket(bucket_name).upload_file(Filename=file_a, Key=file_a)
print('Yas, file uploaded')

# READ and print the file from the bucket
obj = s3.Object(bucket_name, file_a)
body = obj.get()['Body'].read()
print(body)

# UPDATE 'file_a' in the bucket with new content from 'file_b'
s3.Object(bucket_name, file_a).put(Body=open(file_b, 'rb'))
obj = s3.Object(bucket_name, file_a)
body = obj.get()['Body'].read()
print(body)

# DELETE the file from the bucket remove # when ready to run these last 3 commands.
s3.Object(bucket_name, file_a).delete()

# DELETE the bucket (the bucket should be empty.)
#bucket = s3.Bucket(bucket_name)
#bucket.delete()