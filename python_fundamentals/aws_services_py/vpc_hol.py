import boto3
import time
# Create VPC
# we will use a ec2 client
ec2 = boto3.client('ec2')
vpc_name = 'vpc-hol-km'

#this will filter vpcs only with the name we gave so that way another vpc won't continue to get created.
response = ec2.describe_vpcs(
    Filters=[{'Name': 'tag:Name', 'Values': [vpc_name]}]
    )
vpcs = response.get('Vpcs', [])

if vpcs:
    vpc_id = vpcs[0]['VpcId']
    print(f"VPC '{vpc_name}' with ID '{vpc_id}'already exists.")
else:
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response['Vpc']['VpcId']

    time.sleep(5)
    #will wait 5 seconds before creating tags so as not to get an error. 
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value' : vpc_name}])
    print(f"VPC '{vpc_name}' with ID '{vpc_id}'has been created.")

