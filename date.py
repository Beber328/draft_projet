from datetime import datetime
import sys

def check_date_and_challenges(selected_challenges):
    # Obtenez la date et l'heure actuelles
    date_actuelle = datetime.now()

    # Définissez la date limite
    date_limite = datetime(2023, 1, 31)

    # Comparez la date actuelle avec la date limite
    if date_actuelle > date_limite:
        # Vérifiez le nombre de challenges sélectionnés
        if len(selected_challenges.split(',')) > 11:
            print("Dans les temps")
        else:
            print("En retard sur les challenges")
    else:
        print("Avant la date limite")

if __name__ == "__main__":
    # Vérifiez si le nombre d'arguments est correct
    if len(sys.argv) != 2:
        print("Veuillez fournir les challenges sélectionnés en tant qu'argument.")
        sys.exit(1)

    # Récupérez les challenges sélectionnés depuis les arguments de la ligne de commande
    selected_challenges = sys.argv[1]

    # Vérifiez la date et le nombre de challenges
    check_date_and_challenges(selected_challenges)
