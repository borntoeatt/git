pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/borntoeatt/git.git'
            }
        }
        stage('Run Hello') {
            steps {
                sh 'python3 hello.py --name Jenkins'
            }
        }
    }
}
// This Jenkinsfile defines a simple CI/CD pipeline with two stages: Checkout and Run Hello.