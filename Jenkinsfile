pipeline {
    agent any
    parameters {
        string(name: 'REPO_TO_CLONE', defaultValue: 'https://github.com/jehoshu/Final_Project.git', description: 'Git repository URL')
        string(name: 'BRANCH_TO_MERGE', defaultValue: 'master', description: 'Branch to merge')
    }
    stages {
        stage("Clone repository") {
            steps {
                git branch: "${params.BRANCH_TO_MERGE}", url: "${params.REPO_TO_CLONE}"
            }
        }
        stage("Checkout branch") {
            steps {
                sh "git checkout ${params.BRANCH_TO_MERGE}"
            }
        }
        stage("Install dependencies") {
            steps {
                sh "sudo apt-get install python3-venv -y"
                sh "sudo apt-get install python3-pip -y"
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip3 install -r requirements.txt"
            }
        }
        stage("Run merge script") {
            steps {
                sh "python3 project.py"
            }
        }
        stage("Build image") {
            steps {
                sh "docker build --build-arg REPO_TO_CLONE=${params.REPO_TO_CLONE} --build-arg BRANCH_TO_MERGE=${params.BRANCH_TO_MERGE} -t merge-image ."
            }
        }
        stage("Run container") {
            steps {
                sh "docker run -e REPO_TO_CLONE=${params.REPO_TO_CLONE} -e BRANCH_TO_MERGE=${params.BRANCH_TO_MERGE} merge-image"
            }
        }
    }
}