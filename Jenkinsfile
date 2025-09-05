pipeline {
    agent any

    stages {
        stage('Run Hello') {
            steps {
                // Get the latest Git commit author
                script {
                    def author = sh(script: "git log -1 --pretty=format:'%an'", returnStdout: true).trim()
                    // Run your Python script with the commit author as the name
                    sh "python3 hello.py --name \"${author}\""
                }
            }
        }
    }
}

// This Jenkinsfile defines a simple CI/CD pipeline with two stages: Checkout and Run Hello.