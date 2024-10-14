import random

def surveiller_bande_passante(seuil_bande, max_iterations):
    exceed_count = 0
    for iteration in range(1, max_iterations + 1):
        debit_reseau = random.randint(50, 150)  # Simule des valeurs de débit entre 50 et 150 Mbps
        
        if debit_reseau > seuil_bande:
            exceed_count += 1
            print(f"Iteration {iteration}: Débit réseau {debit_reseau} Mbps dépasse le seuil de {seuil_bande} Mbps.")
        else:
            exceed_count = 0
            print(f"Iteration {iteration}: Débit réseau {debit_reseau} Mbps est sous contrôle.")
        
        # Si le débit est dépassé 3 fois de suite
        if exceed_count >= 3:
            print("Alerte : Débit réseau excessif détecté 3 fois consécutivement. Connexion coupée.")
            break

# Exemple d'utilisation
surveiller_bande_passante(100, 10)
