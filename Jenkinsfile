pipeline {
    agent any

    stages {
        stage('TestBuild') {
            steps {
               sh 'pwd'
               sh 'aws sts get-caller-identity'
               sh 'aws s3 ls '
              
            }
        }
    }
}