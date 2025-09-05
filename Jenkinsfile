pipeline {
    agent any

    stages {
        stage('Run Hello') {
            steps {
                // The repository is already checked out by Jenkins using the SCM credentials,
                // so we don’t need another 'git' command here.
                sh 'python3 hello.py'
            }
        }
    }
}

// This Jenkinsfile defines a simple CI/CD pipeline with two stages: Checkout and Run Hello.