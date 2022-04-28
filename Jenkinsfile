pipeline {
    agent any

    stages {
        stage('TestBuild') {
            steps {
               sh 'pwd'
               sh 'export AWS_ACCESS_KEY_ID=AKIA6PM77XAMJGMHGP3V'
               sh 'export AWS_SECRET_ACCESS_KEY=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'
               sh 'export AWS_DEFAULT_REGION=us-east-1'
               sh 'aws s3 ls '
              
            }
        }
    }
}