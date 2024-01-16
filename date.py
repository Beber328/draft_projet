pipeline {
    agent any
    parameters {
        string(name: "NOM", description: 'Entrez votre nom')
        string(name: "PRENOM", description: 'Entrez votre prénom')
        password(name: "Projet_DevOps", description: 'Entrer un mot de passe')
        extendedChoice(
            name: 'CHALLENGES',
            description: 'Sélectionnez les challenges du mois que vous souhaitez faire :',
            multiSelectDelimiter: ',',
            type: 'PT_MULTI_SELECT',
            value: '',
            groovyScript: """
                return [
                    "Janvier | Commencer à écrire un journal",
                    "Fevrier | Faire de votre maison un espace agréable",
                    "Fevrier | Déconnecter du reste du monde et où faire son nid",
                    "Mars | Méditer avoir plus de temps pour soi",
                    "Mars | Mieux manger",
                    "Mars | Faire plus d'exercice",
                    "Mars | Arrêter de fumer",
                    "Avril | Faire des petits gestes",
                    "Avril | Dire des paroles aimables",
                    "Mai | Prenez des cours de salsa",
                    "Mai | Inscrivez-vous à un marathon",
                    "Juin | Sortir dîner",
                    "Juin | Passer du temps avec les vôtres",
                    "Juillet | Profiter des grandes vacances",
                    "Juillet | Profiter des festivals",
                    "Aout | Prendre une couverture"
                ]
            """
        )
    }
    stages {
        stage('Afficher les paramètres') {
            steps {
                echo "Nom: ${params.NOM}"
                echo "Prénom: ${params.PRENOM}"
                echo "Mot de passe: ${params.Projet_DevOps}"
                echo "Challenges : ${params.CHALLENGES}"
            }
        }

        stage('Exécuter le script Python') {
            steps {
                script {
                    // Échapper les guillemets doubles dans les challenges pour éviter les erreurs de syntaxe
                    def escapedChallenges = params.CHALLENGES.replaceAll('"', '\\"')

                    // Exécuter le code Python à partir du fichier date.py avec les challenges sélectionnés
                    def result = bat(script: "python date.py \"${escapedChallenges}\"", returnStatus: true)
                    // Afficher la sortie de l'exécution
                    echo "Résultat de l'exécution du script : ${result}"

                    // Envoi du nombre de challenges au script Python ci-dessus
                    def pythonResult = bat(script: "python script.py \"${escapedChallenges}\"", returnStatus: true)
                    // Afficher la sortie du script Python ci-dessus
                    echo "Résultat de l'exécution du script Python : ${pythonResult}"
                }
            }
        }
    }
}
