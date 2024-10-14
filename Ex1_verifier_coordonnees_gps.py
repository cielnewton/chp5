def verifier_coordonnees_gps(nombre_appareils):
    compteur_appareils_a_verifier = 0

    for i in range(1, nombre_appareils + 1):
        # Saisie des coordonnées pour chaque appareil
        latitude = float(input(f"Entrez la latitude de l'appareil {i} : "))
        longitude = float(input(f"Entrez la longitude de l'appareil {i} : "))

        # Vérification de la validité des coordonnées
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            print(f"Appareil {i}: Coordonnées valides - Latitude: {latitude}, Longitude: {longitude}")
        else:
            print(f"Appareil {i}: Coordonnées invalides - Latitude: {latitude}, Longitude: {longitude}")
            compteur_appareils_a_verifier += 1

    # Résultat final
    if compteur_appareils_a_verifier > 0:
        print(f"{compteur_appareils_a_verifier} appareil(s) à vérifier.")
    else:
        print("Toutes les coordonnées sont valides.")

# Exemple d'utilisation : Vérifier 3 appareils
verifier_coordonnees_gps(3)
