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
        if selected_challenges > 8:
            print("Dans les temps")
        else:
            print("En retard sur les challenges")
    else:
        print("Avant la date limite")

if __name__ == "__main__":
    # Vérifiez si le nombre d'arguments est correct
    if len(sys.argv) != 2:
        print("Veuillez fournir le nombre de challenges sélectionnés en tant qu'argument.")
        sys.exit(1)

    # Récupérez le nombre de challenges sélectionnés depuis les arguments de la ligne de commande
    selected_challenges = int(sys.argv[1])

    # Vérifiez la date et le nombre de challenges
    check_date_and_challenges(selected_challenges)
