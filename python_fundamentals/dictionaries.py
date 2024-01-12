"""Create a dictionary of AWS services and modify the dictionary appropriately."""
def main():
    # Create a dictionary of AWS services and their descriptions as key values.
    aws_services = {
        "S3": "Simple storage service for object storage", 
        "Lambda": "Serverless compute service",
        "EC2": "Elastic compute cloud"
    }

    # Print the dictionary
    print("Simple dictionary of AWS services and descriptions:")
    print(aws_services)

    # Access the description of an item in the dictionary using the key
    lambda_description = aws_services["Lambda"]
    print(f"\nDescription of lambda: {lambda_description}")

    # Modify the description of a service
    aws_services["Lambda"] = "AWS Serverless compute service"
    print(f"\nUpdated description of lambda: {aws_services}")

    # Add a new service and its description to the dictionary
    aws_services["SNS"] = "Simple Notification Service"
    print(f"\nAdded SNS: {aws_services['SNS']}")

    # Remove the ... service from the dictionary
    del aws_services["Lambda"]
    print(f"\nRemoved Lambda: {aws_services}")

    # Use the keys(), values(), and items() methods to display different aspects of the dictionary
    print(aws_services.keys())
    print(aws_services.values())
    print(aws_services.items()) #.items will print the items out in tuple form

    # Modify the dictionary to add a nested structure with additional information (launch_year)
    aws_services["EC2"] = {
        "description": "Elastic compute cloud",
        "launch_year": 2006
    }
    # Print the modified dictionary with nested structure
    print("\nModified dictionary with nested structure:")
    print(aws_services["EC2"])

if __name__ == "__main__":
    main()


