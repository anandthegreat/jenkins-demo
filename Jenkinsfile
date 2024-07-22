pipeline {
    agent any
    stages {
        stage("Setup") {
            steps {
                sh 'pip3 install ruamel.yaml'
                sh 'pip3 install pandas'
            }
        }
        stage("Build") {
            steps {
                sh 'python src/calc_demo.py'
            }
        }
        stage("Test") {
            steps {
                sh 'pytest tests/test_calc.py'
            }
        }
        stage("Deploy") {
            steps{
                echo "Successfully deployed python application"
            }
        }
    }
    post {
        always {
            mail to: 'anand.ve.verma@oracle.com',
            subject: "Jenkins Demo Pipeline #${env.BUILD_NUMBER} Build Completed",
            body: "Check more details here ${env.BUILD_URL}"
        }
    }
}