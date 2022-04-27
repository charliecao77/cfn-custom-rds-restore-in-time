pipeline {
    agent any

    stages {
        stage('TestBuild') {
            steps {
               sh 'pwd'
               sh 'sudo ls -l ~/.aws/'
               sh 'aws sts get-caller-identity'
              
            }
        }
    }
}