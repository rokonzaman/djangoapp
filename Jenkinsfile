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
                sh "docker build . -t kworker3.rokon.local:5000/django:${DOCKER_TAG}"
            }
        }

        stage('Push Image'){
            steps{
  //        withCredentials([string(credentialsId: 'dockerhub', variable: 'dockerHubPwd')]) {
  //            sh "docker login -u rokonzaman -p ${dockerHubPwd}"
                sh "docker push kworker3.rokon.local:5000/django:${DOCKER_TAG}"
            }
        }
    }

        stage('Remove Image'){
            steps{
                sh "docker rmi kworker3.rokon.local:5000/django:${DOCKER_TAG}"
            }
        }

        stage('Deploy to k8s'){
            steps{
                sh "chmod +x changeTag.sh"
                sh "./changeTag.sh ${DOCKER_TAG}"
                sh " kubectl apply -f django-Development.yaml"
            }
        }
    }
}


def getDockerTag(){
    def tag = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
