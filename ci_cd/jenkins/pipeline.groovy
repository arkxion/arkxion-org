pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.10"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r docker/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest src/app --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'pip install bandit safety'
                sh 'bandit -r src/app'
                sh 'safety check -r docker/requirements.txt'
            }
        }
    }
}
