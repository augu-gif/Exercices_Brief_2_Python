pi = 3.141592653589793
E = 2.718281828459045
def carre(x):
  resultat = x*x
  return resultat
def cube(x):
  resultat = x*x*x
  return resultat
def factorielle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat
def valeur_absolue(x):
    if x < 0:
        return -x
    return x
def maximum(liste):
    resultat = liste[0]
    for valeur in liste:
        if valeur > resultat:
            resultat = valeur
    return resultat
def minimum(liste):
    resultat = liste[0]
    for valeur in liste:
        if valeur < resultat:
            resultat = valeur
    return resultat
def moyenne(liste):
    return sum(liste) / len(liste)
def ecart_type(liste):
    moy = moyenne(liste)
    somme = 0

    for valeur in liste:
        somme += (valeur - moy) ** 2

    return (somme / len(liste)) ** 0.5
def mediane(liste):
    nombres = sorted(liste)
    n = len(nombres)
    milieu = n // 2
    if n % 2 == 1:
        return nombres[milieu]
    else:
        return (nombres[milieu - 1] + nombres[milieu]) / 2