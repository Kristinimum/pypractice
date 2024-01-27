"""This script manages EC2 istances using boto3 Python SDK.
"""

# import statements
import boto3

# create ec2 resource and instance name
ec2 = boto3.resource('ec2')
instance_name = 'kmm-ec2-hol'

# store instance id. this none is neither true nor false
instance_id = None
# check if instance which you are trying to create already exists.
# and only work with an instance that has not been terminated. create a list called instances.
#before this code we ran line 30's code to make an instance. so we don't keep creating new instances
# we then used this for loop to iterate through the list of instances to only work with the instance we created. 
#instances = ec2.instances.all()
#instance_exists = False

#for instance in instances:
 #   for tag in instance.tags:
  #      if tag['Key'] == 'Name' and tag['Value'] == instance_name:
   #         instance_exists = True
    #        instance_id = instance.id
     #       print(f"An instance named '{instance_name}' with id '{instance_id}' already exists.")
      #      break
    #if instance_exists:
     #   break

#if not instance_exists:   # then we indented everything else below by 4 spaces.
#Launch a new ec2 Instance if it hasn't already been created
new_instance = ec2.create_instances(
        ImageId='ami-0a3c3a20c09d6f377',  #i did this replace with a valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='jenkins-kp',  # replace with your key pair name
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    },
                ]
            },
        ]
    )
instance_id = new_instance[0].id
print(f"Instance named '{instance_name}' with id '{instance_id}' created.")
# Stop an instance. stop, start, terminate are all functions.
#ec2.Instance(instance_id).stop()
#print(f"Instance '{instance_name}--{instance_id}' has been stopped.")
# Start an instance
#ec2.Instance(instance_id).start()
#print(f"Instance '{instance_name}--{instance_id}' has been started.")
#Terminate an instance
#ec2.Instance(instance_id).terminate()
#print(f"Instance '{instance_name}--{instance_id}' has been terminated.")