# Ouverture du fichier a lire et ecrire (mode "r+" read write)

nomFichier = "a_modifier.txt"
# Le plus faicle est de mettre le fichier à ouvrir dans le meme répertoire
# que ce programme Python.
# Sinon, MODIFIER le nom ci-dessus en donnant le chemin absolu du fichier, du type :
# sous windows : C:\\Users\\Fred\\Documents\\bazar_NSI\\a_modifier.txt
# sous Linux et OsX : /Users/frederic/1ere_NSI/a_modifier.txt
# sous windows il faut doubler les "\”, si ça met un message d'erreur essayer de remplacer les \\ par /
# éviter les espaces dans les noms de dossiers et de fichiers
fichierInit = open(nomFichier, "r", encoding="utf-8")

# ouverture ou creation d'un nouveau fichier s'il n'existe pas lors du "open"
fichierCopie = open ("copie.txt", "w", encoding="utf-8")
# si une erreur s'affiche essayer :
# fichierCopie = open ("copie.txt", "a")

# affichage du contenu du fichier par ligne
for line in fichierInit:
    print(line)

# repositionnement au debut du fichier et lecture d'une ligne
fichierInit.seek(0)
print(fichierInit.readline())

# Recopie ligne par ligne dans le fichier "copie.txt"
# On pourrait aussi bien faire une copie globale (plus rapide)
fichierInit.seek(0)         # repositionnement au debut du fichier
for ligne in fichierInit:
    fichierCopie.write(ligne)

fichierCopie.seek(0,2)   # positionnement a la fin du fichier
                        # Oieme bit avant la fin (2)
fichierCopie.write("bonjour")  # on ne peut ecrire que des chaines de caracteres

print("lecture du fichier intial")
fichierInit.seek(0)
print(fichierInit.read())

print("lecture du fichier copie")
fichierCopie.close() # Fermeture du fichier destination
fichierCopie = open ("copie.txt", "r", encoding="utf-8") # et on le réouvre pour le lire
fichierCopie.seek(0)
print(fichierCopie.read())


fichierInit.close() # Fermeture du fichier source
fichierCopie.close() # Fermeture du fichier destination
