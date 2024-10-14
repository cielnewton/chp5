
import random

# Fonction qui simule l'analyse des logs SSH
def analyser_logs_ssh(nb_tentatives):
    echec_consecutif = 0  # Compteur pour suivre les échecs consécutifs
    
    # Boucle pour simuler les tentatives de connexion
    for tentative in range(1, nb_tentatives + 1):
        # Simule une tentative réussie ou échouée (1 = réussie, 0 = échouée)
        reussite = random.randint(0,1)  
        
        if reussite == 1:
            echec_consecutif = 0  # Réinitialiser les échecs consécutifs
            print(f"Tentative {tentative}: Connexion réussie.")
        else:
            echec_consecutif += 1  # Incrémenter les échecs consécutifs
            print(f"Tentative {tentative}: Connexion échouée.")
        
        # Si trois échecs consécutifs sont détectés
        if echec_consecutif >= 3:
            print("Alerte : Trois connexions échouées consécutives. Compte bloqué.")
            break

# Exemple d'utilisation
analyser_logs_ssh(10)  # Simule 10 tentatives de connexion
