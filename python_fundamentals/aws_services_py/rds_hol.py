import boto3  #watch video 52 and 53 when you run this script.
import time

# Instantiate a botot3 client for RDS. #only have access to RDS with client, not resource.
rds = boto3.client('rds')

# User defined variables
username = 'kmm-user-1'
password = 'zlhgkhytn'
db_subnet_group = 'vpc-hol-km'  #use the vpc id from the one you created in vpc_hol.py. in AWS create DB subnet group. in description use:subnet group used during RDS hol 
db_cluster_id = 'rds-hol-cluster'

# Create the DB cluster in try block we are saying we have a cluster already created we want to use.
try:
    response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
    print(f"The Database Cluster named '{db_cluster_id}' already exists. Skipping creation.")
except rds.exceptions.DBClusterNotFoundFault:
    response = rds.create_db_cluster(
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.08.3',  #this will make it for version1 aurora
        DBClusterIdentifier=db_cluster_id, 
        MasterUsername=username,  
        MasterUserPassword=password,  
        DatabaseName='rds_hol_db',
        DBSubnetGroupName=db_subnet_group,  
        EngineMode='serverless',
        EnableHttpEndpoint=True,
        ScalingConfiguration={
            'MinCapacity': 1, # Minimum ACU
            'MaxCapacity': 8, # Maximum ACU
            'AutoPause': True,
            'SecondsUntilAutoPause': 3600  # Pause after 5 minutes of inactivity
        }
    )
    print(f"The DB cluster named '{db_cluster_id}' has been created.")

    # Wait for the DB cluster to become available. while true is apart of the except response.
    while True:
        response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
        status = response['DBClusters'][0]['Status']
        print(f"The status of the cluster is '{'status'}'")
        if status == 'available':
            break #this will break us from the while loop.

        print("Waiting for the DB Cluster to become available...")
        time.sleep(40)

# Modify the DB cluster. Update the scaling configuration for the cluster.
response = rds.modify_db_cluster(
        DBClusterIdentifier=db_cluster_id, 
        ScalingConfiguration={
            'MinCapacity': 1, # Minimum ACU
            'MaxCapacity': 16, # Maximum ACU
            'SecondsUntilAutoPause': 3600  # Pause after 10 minutes of inactivity
        }
    )
print(f"Updated the scaling configuration for DB cluster '{db_cluster_id}'.")

# Delete the DB the cluster.
"""response = rds.delete_db_cluster(
        DBClusterIdentifier=db_cluster_id, 
        SkipFinalSnapshot = True
    )
print(f"The DB cluster '{db_cluster_id}' is being deleted.")
"""