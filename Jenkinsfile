pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        FUNCTION_NAME = 'atharva-lambda'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/atharvalavangare/atharva-lambda-pipeline.git'
            }
        }

        stage('Zip Lambda') {
            steps {
                sh 'zip function.zip lambda_function.py'
            }
        }

        stage('Deploy Lambda') {
            steps {
                sh '''
                    aws lambda update-function-code \
                      --function-name $FUNCTION_NAME \
                      --zip-file fileb://function.zip
                '''
            }
        }
    }
}
