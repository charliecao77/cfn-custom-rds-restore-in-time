pipeline {
    agent any

    stages {
        stage('TestBuild') {
            steps {
               sh 'pwd'
               sh 'cat ~/.aws/credentials'
               sh 'aws sts get-caller-identity'
              
            }
        }
    }
}