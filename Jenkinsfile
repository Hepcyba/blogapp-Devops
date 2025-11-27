pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python & install deps') {
            steps {
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
    steps {
        sh '''
          . venv/bin/activate

          # Start the app in background
          nohup python app.py > app.log 2>&1 &
          APP_PID=$!

          # Give the server time to start
          sleep 5

          # Run tests
          pytest --junitxml=test-results.xml
          TEST_EXIT_CODE=$?

          # Stop the app
          kill $APP_PID || true

          # Return pytest exit code to Jenkins
          exit $TEST_EXIT_CODE
        '''
    }
}

    }

    post {
        always {
            junit 'test-results.xml'
        }
        success {
            echo '✅ Build & tests passed successfully!'
        }
        failure {
            echo '❌ Build or tests failed – check the console log and test report.'
        }
    }
}
