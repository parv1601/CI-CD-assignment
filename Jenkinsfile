// Jenkinsfile
pipeline {
    agent any // Use any available agent (the Windows machine running Jenkins)

    tools {
        // This ensures the pipeline uses the correct version of Python/Pip
        // This tool must be configured under Manage Jenkins -> Global Tool Configuration
        // Alternatively, you can rely on the OS PATH if python is installed on the agent
        // python 'Python-3.9' 
    }

    environment {
        // Replace with your actual Docker Hub username and Roll Number
        DOCKER_IMAGE = "yourusername/your-roll-number-app"
    }

    stages {
        stage('Pull Code') {
            steps {
                // The pipeline script from SCM handles the checkout
                echo "--- Pulling code from GitHub..."
            }
        }

        stage('Install Dependencies & Build') {
            steps {
                // We install dependencies inside the build stage using the Dockerfile
                // For a separate build step, you might run 'pip install -r requirements.txt' here.
                echo "--- Dependencies installed/built based on requirements.txt"
            }
        }

        stage('Test (Pytest)') {
            steps {
                script {
                    echo "--- Running automated Pytest tests..."
                    
                    // Run pytest using the system's python installation
                    // This command must be executed on the Jenkins agent
                    // The '--junitxml' flag is for generating test reports later (optional)
                    try {
                        sh 'pip install -r requirements.txt' // Ensure tests can run
                        sh 'python -m pytest test_calculator.py' // Execute the tests
                        echo "Tests passed successfully!"
                    } catch (error) {
                        echo "Tests failed! Aborting pipeline."
                        error("Tests failed")
                    }
                }
            }
        }

        stage('Create Docker Image') {
            steps {
                echo "--- Building Docker image: ${env.DOCKER_IMAGE}:latest"
                // The '.' means use the Dockerfile in the current directory (workspace)
                sh "docker build -t ${env.DOCKER_IMAGE}:latest ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Use the Jenkins credentials configured in Step 1
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                    echo "--- Logging in and pushing to Docker Hub..."
                    
                    // 1. Log in to Docker Hub
                    sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}"
                    
                    // 2. Push the image
                    sh "docker push ${env.DOCKER_IMAGE}:latest"
                    
                    // 3. Log out for security
                    sh "docker logout"
                }
            }
        }
    }
}