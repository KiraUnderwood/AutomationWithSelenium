pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent {
                label 'windows'
            }
            steps {
                dir ("C:\\Users\\kira_podlesnaia\\Desktop\\PyProjects\\AutomationWithSelenium"){
                    catchError {
                    bat """
                    .\\venv\\scripts\\pytest.exe -s -v WithSplinterAndPyPOM\\TestEpamPagesWithSplinter.py --alluredir=C:\\Users\\kira_podlesnaia\\workspace\\pytest\\allure-results
                    """
                    }
                }
            }
            
        }
    stage('Reports') {
        agent {
                label 'windows'
            }
        steps{
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'C:\\Users\\kira_podlesnaia\\workspace\\pytest\\allure-results']]
                ])
        }
            }
        
    }
    
}