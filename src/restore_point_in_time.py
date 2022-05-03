import boto3 
import time

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

def restore_db_cluster_to_point_in_time(DBClusterIdentifier, RestoreType, SourceDBClusterIdentifier,RestoreToTime,PubliclyAccessible):
    response = client_rds.restore_db_cluster_to_point_in_time(
        DBClusterIdentifier       = DBClusterIdentifier,
        RestoreType               = RestoreType,
        SourceDBClusterIdentifier = SourceDBClusterIdentifier,
        RestoreToTime             = RestoreToTime,
        PubliclyAccessible        = PubliclyAccessible
    )

    return response

def create_db_instance(DBInstanceIdentifier, DBInstanceClass, DBSubnetGroupName, Engine, DBParameterGroupName, DBClusterIdentifier):
    response = client_rds.create_db_instance(
        DBInstanceIdentifier     = DBInstanceIdentifier,
        DBInstanceClass          = DBInstanceClass,
        Engine                   = Engine,
        DBSubnetGroupName        = DBSubnetGroupName,
        DBParameterGroupName     = DBParameterGroupName,
        #MultiAZ                 = False,
        #AutoMinorVersionUpgrade = False,
        #LicenseModel            = 'postgresql-license',
        #PubliclyAccessible      = False,
        DBClusterIdentifier      = DBClusterIdentifier
    )

    return response


def main():

    DBClusterIdentifier       = 'database-3' 
    RestoreType               = 'full-copy'
    SourceDBClusterIdentifier = 'database-2'
    RestoreToTime             = '2022-05-03T01:30:00Z'
    PubliclyAccessible        =  True
    
    result = restore_db_cluster_to_point_in_time(
        DBClusterIdentifier,
        RestoreType,
        SourceDBClusterIdentifier,
        RestoreToTime,
        PubliclyAccessible
    )
    
    result = descibe_cluster_identifier('database-3')
    dbcluster_status = result["DBClusters"][0]["Status"]
    while dbcluster_status != "available":
        result = descibe_cluster_identifier(DBClusterIdentifier)
        dbcluster_status = result["DBClusters"][0]["Status"]
        print(result["DBClusters"][0]["Status"])
        time.sleep(5) 


    DBInstanceIdentifier = 'database-3-instance-1'
    DBInstanceClass      = 'db.t3.medium'
    DBSubnetGroupName    = 'default-vpc-0ab02ae0ab1d57dd8'
    DBParameterGroupName = 'default.aurora-postgresql13'
    Engine               = 'aurora-postgresql'

    if dbcluster_status == 'available':
        result = create_db_instance(
            DBInstanceIdentifier, 
            DBInstanceClass, 
            DBSubnetGroupName, 
            DBParameterGroupName, 
            DBClusterIdentifier,
            Engine
        )
        print(result)

        result = descibe_db_identifier(DBInstanceIdentifier)
        dbinstance_status = result["DBInstances"][0]["DBInstanceStatus"]
        while dbinstance_status != 'available':
            result = descibe_db_identifier(DBClusterIdentifier)
            dbinstance_status = result["DBInstances"][0]["DBInstanceStatus"]
            print(dbinstance_status)
            time.sleep(5)



if __name__  == "__main__":
    main()


