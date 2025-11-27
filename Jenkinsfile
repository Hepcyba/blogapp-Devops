pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    pytest --junitxml=reports/tests.xml || true
                '''
            }
        }
    }

   post {
    always {
        catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
            junit allowEmptyResults: true, testResults: 'reports/tests.xml'
        }
    }
}

}
