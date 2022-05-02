pipeline {
    agent any
    parameters {
        string(name: 'BucketName', defaultValue: 'charlie-test-cfn-03', description: 'aws s3 bucket for storing Templates')
    }
    stages {
        stage('create S3') {
            steps {
               sh 'aws s3api create-bucket --bucket ${params.BucketName}'
            }
        }
        stage('Build') {
            steps {
               sh 'aws sts get-caller-identity'
               sh './deploy.sh upload'
              
            }
        }
    }
}