import boto3 

session = boto3.Session()
client_rds = session.client('rds')

def descibe_cluster_identifier(DBClusterIdentifier):
    response = client_rds.describe_db_clusters(
        DBClusterIdentifier=DBClusterIdentifier
    )
    return response

def descibe_db_identifier(DBInstanceIdentifier):
    response = client_rds.describe_db_instances(
        DBInstanceIdentifier=DBInstanceIdentifier
    )
    return response

def restore_db_cluster_to_point_in_time(DBClusterIdentifier, RestoreType, SourceDBClusterIdentifier,RestoreToTime):
    response = client_rds.restore_db_cluster_to_point_in_time(
        DBClusterIdentifier       = DBClusterIdentifier,
        RestoreType               = RestoreType,
        SourceDBClusterIdentifier = SourceDBClusterIdentifier,
        RestoreToTime             = RestoreToTime
    )

    return response

def create_db_instance():
    response = client_rds.create_db_instance(
        #DBName = 'test',
        DBInstanceIdentifier='database-3-instance-1',
        DBInstanceClass='db.t3.medium',
        Engine='aurora-postgresql',
        DBSubnetGroupName='default',
        PreferredMaintenanceWindow='mon:03:45-mon:04:15',
        DBParameterGroupName='default.aurora-postgresql13',
        #Port=5432,
        MultiAZ=False,
        AutoMinorVersionUpgrade=False,
        LicenseModel='postgresql-license',
        PubliclyAccessible=False,
        Tags=[
            {
                'Key': 'Name',
                'Value': 'cao'
            },
        ],
        DBClusterIdentifier='database-3'
    )

    return response


def main():
    #result = descibe_cluster_identifier('database-1')
    #print(result)

    #result = descibe_db_identifier('database-1-instance-1')
    #print(result)
    
    #result = restore_db_cluster_to_point_in_time(
    #    'database-1-instance-1',
    #    'full-copy',
    #    'database-1',
    #    '2022-05-02T02:00:00Z'
    #)
    #print(result)

    #result = descibe_cluster_identifier('database-1-instance-1')
    #print(result)

    result = create_db_instance()
    print(result)

    #result = descibe_db_identifier('database-1-instance-2')

    #print(result["DBInstances"][0]["DBInstanceStatus"])

 
if __name__  == "__main__":
    main()


