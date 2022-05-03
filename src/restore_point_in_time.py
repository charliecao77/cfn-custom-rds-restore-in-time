import boto3 
import time

session    = boto3.Session()
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

def create_db_instance(DBInstanceIdentifier, DBInstanceClass, DBSubnetGroupName, Engine, DBParameterGroupName, DBClusterIdentifier):
    response = client_rds.create_db_instance(
        DBInstanceIdentifier     = DBInstanceIdentifier,
        DBInstanceClass          = DBInstanceClass,
        Engine                   = Engine,
        DBSubnetGroupName        = DBSubnetGroupName,
        DBParameterGroupName     = DBParameterGroupName,
        MultiAZ                 = False,
        AutoMinorVersionUpgrade = False,
        LicenseModel            = 'postgresql-license',
        PubliclyAccessible      = False,
        DBClusterIdentifier      = DBClusterIdentifier
    )

    return response


def main():

    DBClusterIdentifier       = 'database-5' 
    RestoreType               = 'full-copy'
    SourceDBClusterIdentifier = 'database-2'
    RestoreToTime             = '2022-05-03T01:30:00Z'
    
    result = restore_db_cluster_to_point_in_time(
        DBClusterIdentifier,
        RestoreType,
        SourceDBClusterIdentifier,
        RestoreToTime
    )
    
    result = descibe_cluster_identifier('database-5')
    dbcluster_status = result["DBClusters"][0]["Status"]
    while dbcluster_status != "available":
        result = descibe_cluster_identifier(DBClusterIdentifier)
        dbcluster_status = result["DBClusters"][0]["Status"]
        print(result["DBClusters"][0]["Status"])
        time.sleep(5) 


    DBInstanceIdentifier = 'database-5-instance-1'
    DBInstanceClass      = 'db.t3.medium'
    DBSubnetGroupName    = 'default'
    DBParameterGroupName = 'default.aurora-postgresql13'
    Engine               = 'aurora-postgresql'

    if dbcluster_status == 'available':
        result = create_db_instance(
            DBInstanceIdentifier, 
            DBInstanceClass, 
            DBSubnetGroupName, 
            Engine, 
            DBParameterGroupName, 
            DBClusterIdentifier
        )
        print(result)

        result = descibe_db_identifier(DBInstanceIdentifier)
        dbinstance_status = result["DBInstances"][0]["DBInstanceStatus"]
        while dbinstance_status != 'available':
            result = descibe_db_identifier(DBInstanceIdentifier)
            dbinstance_status = result["DBInstances"][0]["DBInstanceStatus"]
            print(dbinstance_status)
            time.sleep(5)



if __name__  == "__main__":
    main()


