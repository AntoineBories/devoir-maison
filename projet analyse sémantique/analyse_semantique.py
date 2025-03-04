def champs_lexicaux():
    f1 = open("frenchSTb.txt", "r",encoding ="utf-8 sig")
    f2 = open("stopwords-fr.txt", "r",encoding ="utf-8 sig")
    f3 = open("mots_vides.txt","w",encoding ="utf-8 sig")
    f4 = open("cl_revolte.txt","r",encoding ="utf-8 sig")
    f5 = open("cl_greve.txt","r",encoding ="utf-8 sig")
    f6 = open("cl_amour.txt","r",encoding ="utf-8 sig")
    f7 = open("cl_desir.txt","r",encoding ="utf-8 sig")
    f8 = open("cl_charbon.txt","r",encoding ="utf-8 sig")
    f9 = open("cl_mer.txt","r",encoding ="utf-8 sig")

    mots_vides = list(f1.read().split())
    lf2 = list(f2.read().split())

    for mot in lf2:
        if str(mot) not in mots_vides:
            mots_vides.append(str(mot))


    cl_revolte = list(f4.read().split())
    cl_greve = list(f5.read().split())
    cl_amour = list(f6.read().split())
    cl_desir = list(f7.read().split())
    cl_charbon = list(f8.read().split())
    cl_mer = list(f9.read().split())

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    """
    print("longueur des listes mots vides :",len(list(f1.read().split())),len(lf2))
    print("nombre de mots vides : ",len(mots_vides))
    print(mots_vides[:50])
    print(cl_revolte)
    print('nombre de mots pour le champ lexical "revolte" : ',len(cl_revolte))
    print(cl_greve)
    print('nombre de mots pour le champ lexical "greve" : ',len(cl_greve))
    print(cl_amour)
    print('nombre de mots pour le champ lexical "amour" : ',len(cl_amour))
    print(cl_desir)
    print('nombre de mots pour le champ lexical "desir" : ',len(cl_desir))
    print(cl_charbon)
    print('nombre de mots pour le champ lexical "mine" : ',len(cl_charbon))
    print(cl_mer)
    print('nombre de mots pour le champ lexical "mine" : ',len(cl_mer))
    """
    return mots_vides, cl_revolte, cl_greve, cl_amour, cl_charbon,cl_desir,cl_mer

mots_vides, cl_revolte, cl_greve, cl_amour, cl_charbon,cl_desir,cl_mer = champs_lexicaux()

