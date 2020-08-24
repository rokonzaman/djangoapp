pipeline {
    agent {
        node {
            label 'kmaster'
        }
    }
    environment{
        DOCKER_TAG = getDockerTag()
    }
    stages{

        stage('Git Checkout'){
            steps{
                git credentialsId: 'github', url: 'https://github.com/rokonzaman/djangoapp'
            }
        }

        stage('Build Docker Image'){
            steps{
                sh "docker build . -t rokonzaman/django:${DOCKER_TAG}"
            }
        }

    }
}

def getDockerTag(){
    def tag = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
