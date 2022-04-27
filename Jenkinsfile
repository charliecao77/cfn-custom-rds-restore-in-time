pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               sh 'pwd'
               sh 'export AWS_ACCESS_KEY_ID=AKIA3HYB6HF36LLRZEMB'
               sh 'export AWS_SECRET_ACCESS_KEY=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'
               sh 'export AWS_DEFAULT_REGION=us-east-1'
               sh 'aws sts get-caller-identity'
              
            }
        }
    }
}