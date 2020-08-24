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

        stage('Build Image'){
            steps{
                sh "docker build . -t rokonzaman/django:${DOCKER_TAG}"
            }
        }

        stage('Push Image'){
            steps{
                sh "docker push rokonzaman/django:${DOCKER_TAG}"
            }
        }

    }
}

def getDockerTag(){
    def tag = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
