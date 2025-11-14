pipeline {
    agent any

    environment {
        IMAGE_NAME = "indupriyavempati/blogapp:latest"
        DOCKER_PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/IndupriyaVempati/blogapp-Devops.git'
            }
        }

       stage('Setup Python Environment') {
    steps {
        // Create venv if not exists
        bat 'if not exist venv python -m venv venv'

        // Upgrade pip
        bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'

        // Install all dependencies including pytest
        bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'

        // Install pytest explicitly (to avoid "No module named pytest")
        bat 'venv\\Scripts\\python.exe -m pip install pytest'
    }
}

        stage('Run Tests') {
            steps {
                // Run pytest
                bat 'venv\\Scripts\\python.exe -m pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "\"${env.DOCKER_PATH}\" build -t ${env.IMAGE_NAME} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                // Hardcoded login (username & password)
                bat "\"${env.DOCKER_PATH}\" login -u indupriyavempati -p Priya@2004"
                bat "\"${env.DOCKER_PATH}\" push ${env.IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo '✅ Jenkins Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs.'
        }
    }
}
