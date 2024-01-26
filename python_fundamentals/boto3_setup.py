import boto3_setup

# This creates our resource and assigns it to the s3 variable.
s3 = boto3.resource('s3')

#Use a for loop to loop through the buckets. This gets all buckets using resource and iterates through each bucket.
for bucket in s3.buckets.all():
    print(bucket.name)

#bucket.name calls on the name of the bucket. 
#run in terminal with: python boto3_setup.py
