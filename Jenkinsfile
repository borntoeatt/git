pipeline {
    agent any

    stages {
        stage('Run Hello Party') {
            steps {
                script {
                    // Get the latest Git commit author
                    def author = sh(script: "git log -1 --pretty=format:'%an'", returnStdout: true).trim()

                    // Run the Python script: random greeting & emoji handled inside Python
                    sh """
                        python3 hello.py \
                            --name "${author}" \
                            --build-number "${BUILD_NUMBER}"
                    """
                }
            }
        }
    }
}

// This Jenkinsfile defines a simple CI/CD pipeline with two stages: Checkout and Run Hello.