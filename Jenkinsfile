pipeline {
    agent any

    stages {
        stage('Run Hello Party') {
            steps {
                script {
                    // Get the latest Git commit author
                    def author = sh(script: "git log -1 --pretty=format:'%an'", returnStdout: true).trim()

                    // Optional: pick a random greeting in Groovy
                    def greetings = ["Hello", "Howdy", "Yo", "Greetings", "Salutations", "Sup", "Ahoy", "Hiya"]
                    def randGreeting = greetings[new Random().nextInt(greetings.size())]

                    // Run the Python script with dynamic parameters
                    sh """
                        python3 hello.py \
                            --name "${author}" \
                            --greeting "${randGreeting}" \
                            --build-number "${BUILD_NUMBER}"
                    """
                }
            }
        }
    }
}


// This Jenkinsfile defines a simple CI/CD pipeline with two stages: Checkout and Run Hello.