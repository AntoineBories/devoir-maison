#ici pour le code 
# voie a suivre : 
# - ouvrir le fichier germinal_nettoye.txt, 
# - ajouter chaque mot a un dictionnaire avec comme cle le mot et comme valeur le nombre de fois ou il est apparu 
# - comparer le dictionnaire avec le les fichiers "cl_...."
# - écrire le nom du fichier auquel il y a le plus de similitude 

#ex 1 

def occurrences(chaine) :

    mots = chaine.split()  # Séparer la chaîne en mots
    compteur = {}  # Dictionnaire pour stocker les occurrences
    
    for mot in mots:
        if mot in compteur:
            compteur[mot] = compteur[mot] + 1  # Incrémente si le mot est déjà présent
        else:
            compteur[mot] = 1  # Ajoute le mot au dictionnaire
    
    return compteur


texte = "coucou coucou c est le coucou qui dit coucou ne dit pas bonjour ne dit pas au revoir même pour se revoir"
print(occurrences(texte))

#ex 2

def occ_max(dico, longueur):
    max_mot = None
    max_occ = 0
    
    for mot, occ in dico.items():
        if len(mot) == longueur and occ > max_occ:
            max_mot = mot
            max_occ = occ
    
    return max_mot, max_occ

# Exemple d'utilisation
texte = "coucou coucou c est le coucou qui dit coucou ne dit pas bonjour ne dit pas au revoir même pour se revoir"
dico = occurrences(texte)
print(occ_max(dico, 6))