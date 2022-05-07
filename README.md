# cfn-custom-rds-restore-in-time

# ToDo List:
 - Generate the Templates to create Custom Resource 
 - Tigger the deployment with Jenkins
 - convert the template to Aurora RDS for testing restore point in time

# Generate the Templates to create Custom Resource
 - create root.yml
    - the Template root template  
 - create role.yml
    - provision a role for assisting lambda running
 - create lambda.yml
    - provision a lambda for custom resource provider
 - create custom_simple.yml
    - create the custom resource by template developer


 

# Test the RDS restore point in time
Cloudformation Template for Aurora RDS creation/restore point in time
- create Aurora RDS cluster with one master instance
- generate the automatic snapshot by change the backup time 
- restore the Aurora RDS with the custom resource 

# Test Environment Initial
- using the acloudguru box
- setup the aws environment variables
    - export AWS_ACCESS_KEY_ID=
    - export AWS_SECRET_ACCESS_KEY=
    - export AWS_DEFAULT_REGION=
- git clone https://github.com/charliecao77/cfn-custom-rds-restore-in-time.git

- cd cfn-custom-rds-restore-in-time
- optional, update the S3 bucket name in deploy.sh
- optional, sh deploy.sh create # create S3 bucket 
- optional, sh deploy.sh # without creating S3 bucket
