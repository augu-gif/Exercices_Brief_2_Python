def somme_cumulee(liste):
    resultat = []
    somme = 0

    for nombre in liste:
        somme += nombre
        resultat.append(somme)

    return resultat
def compter_occurrences(liste):
    resultat = {}

    for element in liste:
        if element in resultat:
            resultat[element] += 1
        else:
            resultat[element] = 1

    return resultat
def inverser_dict(dictionnaire):
    resultat = {}

    for cle, valeur in dictionnaire.items():
        resultat[valeur] = cle

    return resultat
def filtrer_pairs(liste):
    resultat = []

    for nombre in liste:
        if nombre % 2 == 0:
            resultat.append(nombre)

    return resultat
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
def trouver_doublons(liste):
    vus = []
    doublons = []

    for element in liste:
        if element in vus:
            if element not in doublons:
                doublons.append(element)
        else:
            vus.append(element)

    return doublons
def calculer_moyenne_ponderee(valeurs, poids):
    somme_ponderee = 0
    somme_poids = 0

    for i in range(len(valeurs)):
        somme_ponderee += valeurs[i] * poids[i]
        somme_poids += poids[i]

    return somme_ponderee / somme_poids
    