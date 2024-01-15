import sys

# Récupérer les challenges depuis les arguments de la ligne de commande
selected_challenges = sys.argv[1].split(',')

# Compter le nombre de challenges sélectionnés
challenges_count = len(selected_challenges)

# Afficher le résultat
print(f"Nombre de challenges sélectionnés : {challenges_count}")
