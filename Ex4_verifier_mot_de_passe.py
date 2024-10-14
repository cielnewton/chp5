def verifier_mot_de_passe():
    # Mot de passe prédéfini
    mot_de_passe_correct = "admin123"
    tentatives_restantes = 3

    # Boucle pour permettre jusqu'à 3 tentatives
    while tentatives_restantes > 0:
        # Demande à l'utilisateur de saisir son mot de passe
        mot_de_passe = input("Veuillez entrer votre mot de passe : ")

        # Vérification du mot de passe
        if mot_de_passe == mot_de_passe_correct:
            print("Accès autorisé.")
            return  # Arrête la fonction si le mot de passe est correct

        # Si le mot de passe est incorrect
        tentatives_restantes -= 1
        print(f"Mot de passe incorrect. Il vous reste {tentatives_restantes} tentative(s).")

        # Si c'était la dernière tentative
        if tentatives_restantes == 0:
            print("Alerte : Accès bloqué après 3 tentatives échouées.")
            return  # Arrête la fonction après 3 tentatives échouées

# Appel de la fonction
verifier_mot_de_passe()
