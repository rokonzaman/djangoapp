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
                    userRemoteConfigs: [[url: 'https://github.com/rokonzaman/djangoapp.git']]
                ])
            }
        }

        stage('Deploy Master') {
                when {
                    branch 'master'
                }
                steps {
                    sh """
                    echo "Create Image"
                    echo "Push Image"
                    echo "kubernetes deployment"
                    """

                    sh """
                    echo "Deploying Code"
                    """
                }
            }

        }
    }
