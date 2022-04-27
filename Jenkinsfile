pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               sh 'pwd'
               sh './deploy.sh create'
              
            }
        }
    }
}