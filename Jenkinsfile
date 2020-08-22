pipeline {

    agent {
        node {
            label 'kmaster'
        }
    }

    options {
        buildDiscarder logRotator(
                    daysToKeepStr: '16',
                    numToKeepStr: '10'
            )
    }


 stages {
    stage('Code Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/spring-projects/spring-petclinic.git']]
                ])
            }
        }

        stage('Build Deploy Code') {
                when {
                    branch 'develop'
                }
                steps {
                    sh """
                    echo "Building Artifact"
                    """

                    sh """
                    echo "Deploying Code"
                    """
                }
            }

        }
    }
