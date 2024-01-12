"""Create variables of different data types and display times.
"""

def main():
    # String (str)
    instance_type = "t2.micro"
    message = "My instances are of type: "

    # Integar (int)
    num_of_instances = 5
    hours_running = 10

    print(f"{message} {instance_type}. I have {num_of_instances} \nof them and they have been running {hours_running} hours.")

    # Boolean (bool)
    instances_running = True
    print(f"Are my instances running? {instances_running}.")
    print(f"My variable is of type: {type(instances_running)}.")

    # Floating point number (float)



if __name__ == "__main__":
    main()