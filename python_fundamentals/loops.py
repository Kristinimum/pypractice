"""Use a list of AWS services and demonstrate various loop operations.
"""

def main():
    aws_services = ['S3', 'Lambda', 'EC2', 'RDS', 'DynamoDB']
    print(f"AWS services list: {aws_services}")

    # Use a for loop to iterate through a list. definit iteration
    #print("\nUsing a for loop to iterate through the list:")
    for service in aws_services:
        print(service)

    # Use a while loop to iterate through the list in reverse order. indefinite iteration
    # need to specify the index so will know how many times it needs to run.
    # Since we start at 0 with index we also need to subtract 1
    print("\nUsing a while loop to iterate through the list in reverse order:")
    index = len(aws_services) - 1
    while index >= 0:       #inclduing the >= will include the 0 index spot which is S3.
        print(aws_services[index])
        index -= 1 #this means when index is no longer greater than 0 it will stop.

#Be careul with while loops that run forever.
    # Using enumerate() with a for loop to get both index and value
    print("\nUsing enumerate() with a for loop to get both index and value:")
    for index, service in enumerate(aws_services):
        print(f"Service # {index}: {service}.")
#This prints out:
#Service # 0: S3.
#Service # 1: Lambda.
#Service # 2: EC2.
#Service # 3: RDS.
#Service # 4: DynamoDB.
# To start the services at 1 and not 0, add a + 1 in the {index}
    for index, service in enumerate(aws_services):
        print(f"Service # {index + 1}: {service}.")
#This prints out
#Service # 1: S3.
#Service # 2: Lambda.
#Service # 3: EC2.
#Service # 4: RDS.
#Service # 5: DynamoDB.

if __name__ == "__main__":
    main()    