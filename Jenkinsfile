pipeline {
    agent any
    parameters {
        string(name: 'BucketName', defaultValue: 'charlie-test-cfn-03', description: 'aws s3 bucket for storing Templates')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
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