pipeline{
    agent any
    environment{
        registry= "techinnova/jenkins-ejercicio"
        registryCredentials="dockerhub"
        project="jenkins-ejercicio"
        projectVersion="1.0"
        repository="git@github.com:carlostechinnovation/curso-devops-a1-carlos.git"
        repositoryCredentials="github"
    }
    stages{
        stage('Limpiar Workspace'){
            steps{
                cleanWs()
            }
        }
        stage('Checkout codigo'){
            steps{
                script{
                    git branch: 'main',
                        credentialsId: repositoryCredentials,
                        url: repository
                }
            }
        }

        stage('Calidad de codigo y seguridad'){
            environment{
                scannerHome= tool 'Sonar'
            }
            steps{
                script{
                    withSonarQubeEnv('Sonar'){
                        sh "${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=$project \
                        -Dsonar.projectName=$project \
                        -Dsonar.projectVersion=$projectVersion \
                        -Dsonar.sources=./"
                    }
                }
            }
        }

        stage('Construir imagen'){
            steps{
                script{
                    dockerImage= docker.build registry
                }
            }
        }

        stage('Test ejecucion y borrar contenedor de test'){
            steps{
                script{
                    try{
                        sh 'docker run --name $project -e "MIVARIABLE=99" $registry'
                    }finally{
                        sh 'docker rm $project'
                    }

                }
            }
        }

        stage('Push en dockerhub'){
            steps{
                script{
                    docker.withRegistry('',registryCredentials ){
                        dockerImage.push()
                    }
                }
            }
        }

    }
    post{
        failure{
            echo 'El pipeline ha fallado.'
        }
    }
}