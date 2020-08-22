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

        stage('Deploy Master') {
                when {
                    branch 'master'
                }
                steps {
                    sh """
                    echo "Create Image"
                    docker build -t rokonzaman/master_django:latest /root/jenkins-agent/workspace/Multibranch_master/.
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
