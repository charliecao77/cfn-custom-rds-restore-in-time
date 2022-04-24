
export AWS_ACCESS_KEY_ID=AKIAUE6WQKX32ML4KU53
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=us-east-1

aws sts get-caller-identity

aws s3 ls 

#upload CFN
aws s3 cp ./cfn/s3.yml s3://charlie-test-rds-restore-point-in-time/

#CFN Stack Set
testcase='s3'
StackName="charlie-test-$testcase"

aws cloudformation create-stack \
--stack-name $StackName \
--template-url s3://charlie-test-rds-restore-point-in-time/s3.yml 
#--parameters ParameterKey=KeyPairName,ParameterValue=TestKey ParameterKey=SubnetIDs,ParameterValue=SubnetID1\\,SubnetID2


