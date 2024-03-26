import random
import matplotlib.pyplot as plt
dic = {}
nom_fichier = ""

    
def calculFinale(num:int) -> chr:
    if num < 50:
        return "E"
    elif num < 60:
        return "D"
    elif num < 70:
        return "C"
    elif num < 80:
        return "B"
    else: return "A"

def charger_liste_etudiants ():
# Implémentez la logique de chargement ici 
    nom_fichier = input('Entrez le nom du fichier dans le format "exemple.txt" : ')
    try:
        f = open(nom_fichier, "r")
        print("Fichier ouvert")
        for i in f:
            prenom, nom = i.strip().split(",")
            dic[i]={"Prénom":prenom,
                         "Nom": nom,
                         'TP1': None,
                         'TP2': None,
                         'TP3': None,
                         'Examen1':None,
                         'Examen2':None,
                         'NoteNumFinale':None,
                         'NoteAlphaFinale':None
                         }
        print("Liste d'étudiants chargée avec succès.")
        f.close()
    except Exception as e:
        print(f"Erreur  : fichier non-trouvé!\n{e}")
 
def afficher_liste_etudiants ():

    if len(dic) == 0:
        print("La liste d'étudiants est vide. Veuillez charger une liste d'étudiants.")
    
    else:
        for i in dic:
            print(f"{dic[i]['Prénom']}, {dic[i]['Nom']} | TP1 : {dic[i]['TP1']} TP2 : {dic[i]['TP2']} TP3 : {dic[i]['TP3']} Examen1 : {dic[i]['Examen1']} Examen2 : {dic[i]['Examen2']} NoteNumFinale : {dic[i]['NoteNumFinale']} NoteAlphaFinale : {dic[i]['NoteAlphaFinale']}\n")



def ajouter_generer_notes ():
    for i in dic:
            tp1 = random.randint(0,10)
            tp2 = random.randint(0,10)
            tp3 = random.randint(0,10)
            exm1 = random.randint(0,35)
            exm2 = random.randint(0,35)
            alphaNumFinale  =  tp1 + tp2 + tp3 + exm1 + exm2
            alphaFinale = calculFinale(alphaNumFinale)
            dic[i]['TP1'] = tp1
            dic[i]['TP2'] = tp2
            dic[i]['TP3'] = tp3 
            dic[i]['Examen1']= exm1
            dic[i]['Examen2'] = exm2 
            dic[i]['NoteAlphaFinale'] = alphaFinale
            dic[i]['NoteNumFinale'] = alphaNumFinale

    print("Liste d'étudiants génnerée avec succès.")

def enregistrer_notes ():
# Implémentez la logique d'enregistrement ici 
    erg_fichier = input("Entrez le nom du fichier où enregistrer les notes.")
    if erg_fichier == nom_fichier:
        print("Le fichier de sortie ne peut pas avoir le même nom que le fichier original.")
    else:
        f = open(f"{erg_fichier}","w")
        
        for i in dic:
            ligne=f"{dic[i]['Prénom']}, {dic[i]['Nom']}, {dic[i]['TP1']}, {dic[i]['TP2']}, {dic[i]['TP3']}, {dic[i]['Examen1']}, {dic[i]['Examen2']}, {dic[i]['NoteNumFinale']}, {dic[i]['NoteAlphaFinale']}\n"
            f.write(ligne)

def affichage_graphique ():
# Implémentez la logique d'affichage graphique ici 
    plt.bar()
    plt.title("TP1")
    plt.show()
    pass
def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Charger la liste des étudiants") 
        print("2. Afficher la liste des étudiants et leurs notes") 
        print ("3. Ajouter et générer des notes")
        print("4. Enregistrer les notes")
        print("5. Affichage graphique des notes")
        print("6. Quitter")
        choix = input("Veuillez choisir une option (1-6): ")
        
        if choix == '1':
            charger_liste_etudiants ()
        elif choix == '2':
            afficher_liste_etudiants()
        elif choix == '3':
            ajouter_generer_notes ()
        elif choix == '4':
            enregistrer_notes ()
        elif choix == '5':
            affichage_graphique ()
        elif choix == '6':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
                

        
menu_principal ()