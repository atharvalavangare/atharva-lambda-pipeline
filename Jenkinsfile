pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        LAMBDA_FUNCTION_NAME = 'data-processor-lambda'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/atharvalavangare/atharva-lambda-pipeline.git', branch: 'main'
            }
        }

        stage('Zip Lambda') {
            steps {
                sh 'zip function.zip lambda_function.py'
            }
        }

        stage('Deploy Lambda') {
            steps {
                withAWS(region: "${env.AWS_REGION}", credentials: 'aws-jenkins-creds') {
                    sh '''
                    aws lambda update-function-code \
                      --function-name ${LAMBDA_FUNCTION_NAME} \
                      --zip-file fileb://function.zip
                    '''
                }
            }
        }
    }
}
