#!/bin/bash

echo "login AWS console to create the access key/secret key "


echo "Initial AWS CLI Environment"
#export AWS_ACCESS_KEY_ID=AKIA2JXBGFQDIK47X4OK
#export AWS_SECRET_ACCESS_KEY=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
#export AWS_DEFAULT_REGION=us-east-1

CreateBucket=$1
BucketName='charlie-test-cfn-04'

echo "AWS default config"
aws sts get-caller-identity

if [ $CreateBucket == 'create' ] && [ "$1" != '' ];then
  echo "creating AWS S3 bucket $BucketName "
  aws s3api create-bucket --bucket $BucketName
fi


VPVId=$(aws ec2 describe-vpcs --query 'Vpcs[0].VpcId')
SecurityGroupId=$(aws ec2 describe-security-groups --query 'SecurityGroups[0].GroupId')
Subnet01=$(aws ec2 describe-subnets --query 'Subnets[0:1:1].SubnetId' --output text)
Subnet02=$(aws ec2 describe-subnets --query 'Subnets[1:2:1].SubnetId' --output text)
Subnets="${Subnet01}\\,${Subnet02}"
echo "VPC ID: $VPVId"
echo "SecurityGroup ID: $SecurityGroupId"
echo "Subnets: $Subnets"


echo "upload Templates to s3://$BucketName/"
aws s3 sync ./cfn/ s3://$BucketName/

#CFN Stack Set
testcase='s3-02'
#StackName="charlie-test-$testcase-${RANDOM:0:2}"
StackName="charlie-test-$testcase"

aws cloudformation describe-stacks --stack-name $StackName > /dev/null 2>&1
if [ $? -eq 0 ];then
  CFNCommand='update-stack'
else 
  CFNCommand='create-stack'
fi

aws cloudformation $CFNCommand \
--capabilities CAPABILITY_NAMED_IAM \
--stack-name $StackName \
--template-url https://$BucketName.s3.amazonaws.com/root.yml \
--parameters ParameterKey=S3Name,ParameterValue=$BucketName\
 ParameterKey=DatabaseSubnets,ParameterValue="${Subnets}"\
 ParameterKey=DatabaseSecurityGroups,ParameterValue=$SecurityGroupId 


StackStatus=$(aws cloudformation describe-stacks --stack-name $StackName --query "Stacks[0].StackStatus"|tr -d '"')

while [ $StackStatus = "CREATE_IN_PROGRESS" ] || [ $StackStatus = "UPDATE_IN_PROGRESS" ] || [ $StackStatus = "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS" ]
do 
  echo $StackStatus
  StackStatus=$(aws cloudformation describe-stacks --stack-name $StackName --query "Stacks[0].StackStatus"|tr -d '"')
  sleep 5
done

if [ $StackStatus = "CREATE_COMPLETE" ] || [ $StackStatus = "UPDATE_COMPLETE" ] ;then
  echo $StackStatus
  echo "All Good!"
else
  echo $StackStatus
  echo "Stack error out"
fi

echo "Root CFN: root.yml"