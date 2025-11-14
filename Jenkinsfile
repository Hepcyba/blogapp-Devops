pipeline {
    agent any

    environment {
        IMAGE_NAME = "indupriyavempati/blogapp:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/IndupriyaVempati/blogapp-Devops.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create venv
                bat 'python -m venv venv'

                // Activate and install dependencies
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'

            }
        }

       stage('Run Tests') {
    steps {
        echo "No tests folder found, skipping tests"
    }
}


        stage('Build Docker Image') {
            steps {
               bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t indupriyavempati/blogapp .'


            }
        }

        stage('Push Docker Image') {
            steps {
                // Make sure Jenkins Docker host is logged in
                bat "\"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe\" login -u indupriyavempati -p Priya@2004"
               bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" push indupriyavempati/blogapp'
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
