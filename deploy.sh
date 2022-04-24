

echo "login AWS console to create the access key/secret key "


echo "Initial AWS CLI Environment"
export AWS_ACCESS_KEY_ID=AKIA3RMICJBTFP6WHZKZ
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=us-east-1

echo "AWS default config"
aws sts get-caller-identity

echo "Create S3 bucket"
aws s3 mb s3://charlie-test-rds-restore-point-in-time --region $AWS_DEFAULT_REGION

echo "upload CFN"
aws s3 cp ./cfn/s3.yml s3://charlie-test-rds-restore-point-in-time/

#CFN Stack Set
testcase='s3'
StackName="charlie-test-$testcase"

echo "delete Stack"
aws cloudformation delete-stack \
    --stack-name $StackName

echo "create Stack"
aws cloudformation create-stack \
--stack-name $StackName \
--template-url https://charlie-test-rds-restore-point-in-time.s3.amazonaws.com/s3.yml
#--parameters ParameterKey=KeyPairName,ParameterValue=TestKey ParameterKey=SubnetIDs,ParameterValue=SubnetID1\\,SubnetID2

    
