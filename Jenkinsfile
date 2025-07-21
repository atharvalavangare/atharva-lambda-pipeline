pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        FUNCTION_NAME = 'atharva-lambda-demo'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/atharvalavangare/atharva-lambda-pipeline.git'
            }
        }

        stage('Zip Lambda') {
            steps {
                dir('lambda') {
                    sh 'zip -r ../lambda_function_payload.zip .'
                }
            }
        }

        stage('Deploy Lambda') {
            steps {
                sh """
                aws lambda update-function-code \
                  --function-name $FUNCTION_NAME \
                  --zip-file fileb://lambda_function_payload.zip \
                  --region $AWS_REGION
                """
            }
        }
    }
}
