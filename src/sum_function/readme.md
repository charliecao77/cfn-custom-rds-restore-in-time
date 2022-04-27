# 
mkdir sum_function
cd sum_function
pip3 install -t . crheler
# on some systems pip may fail with a distutils error, if you run into this, try running pip with the –system argument
# pip install —system -t . crhelper
touch lambda_function.py


#
cat > trust-policy.json <<'EOL'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOL




aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json

aws iam delete-role --role-name lambda-ex
aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}' > role.tmp
iamArn=$(cat role.tmp |jq ."Role"."Arn")

aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam list-roles

zip -r ../sum.zip ./
aws lambda create-function \
    --function-name "crhelper-sum-resource" \
    --handler "lambda_function.handler" \
    --timeout 900 \
    --zip-file fileb://../sum.zip \
    --runtime python3.9 \
    --role "arn:aws:iam::417055865024:role/lambda-ex"

aws lambda create-function 
--function-name crhelper-sum-resource 
--handler lambda_function.handler 
--timeout 900 
--zip-file fileb://./src/sum.zip 
--runtime python3.9 
--role "arn:aws:iam::169378710542:role/lambda-ex"


aws lambda get-function --function-name crhelper-sum-resource

aws lambda delete-function --function-name crhelper-sum-resource
