import psycopg2
#import mariadb (ne pas utiliser)
#import sqlite3 (ne pas utiliser)
#import mysql.connector (pas besoin)
#from mysql.connector import Error  (pas besoin)
#from psycopg2 import sql (pas utile)
#import uuid (id unique depuis la table ducoup pas besoin)
#import datetime (la table s'en occupe)
conn = (psycopg2.connect
        (database="notes",   #on se co à la database notes créer dans postgres
        user="postgres",    #on y inscrit l'utilisateur paramètrer
        password="1",       #le password assigner à l'user
        host="localhost",   #à quoi on se co
        port="5432"))        #le port qui correspond à postgres par defaut
curs = conn.cursor()
class Note:
    def __init__(self, content, category):  #__init__ défini l'état initial des objets de la class
        # est aussi un constructeur qui initialise les attributs avant d'utiliser un / des objet(s)
        self.content = content
        self.category = category
def nouvellenote():
    content = input("Saisissez le contenue de votre note : ")   #on demande le contenu et la categorie que l'user veut pour sa note
    category = input("Quelle est la catégorie de cette note ? : ")

    new = Note(content, category)

    curs.execute(""" INSERT INTO notes (content, category) 
        VALUES(%s, %s);""", (new.content, new.category))    #vars renvoie au dictionnaire associé à l'objet

    conn.commit()

    print("Bravo !! Votrre note à été créer avec succès!")

    menu()
def tout():
    curs.execute(""" SELECT * FROM notes;""")
    tuple = curs.fetchall()
            #permet de récupérer toutes les lignes restante de l'ensemble des resultats sous une liste de tuples
            #liste de tuples ~~ liste python mais qui utilise moins d'espace
    print(tuple)

    menu()
def selection():
    id = input("Choissiez l'ID de la note que vous souhaitez afficher: ")
    curs.execute(""" SELECT * FROM notes WHERE id = %s;""", (id))   #querry permet d'intéragir avec la base de donnée notes
    #%s reviens à mettre l'id inscrite par l'user
    n = curs.fetchone()
    # fetchone vérifie si n existe bien dans la base de donnée, si n = none alors il n'y a pas d'id existant
    if n is None:   # si n existe alors on l'affiche et on reviens au menu avec les différentes options
        print("L'ID que vous venez d'entrer n'est pas valide ou est n'est pas enregistrer. Merci de saisir un ID valide.")
    else:
        print(n)
    menu()

def modif():
    id = input("Choissiez la note que vous voulez modifier: ")
    curs.execute(""" SELECT id FROM notes WHERE id = %s;""", (id))
    n = curs.fetchone() #on reprend le code d'avant pour trouver id qui à été inscrit par l'user
    if n is None:
        print(  #comme avant si l'id de la note n'existe pas on renvoie ce message d'erreur et on renvoie au menu
            "L'ID que vous venez d'entrer n'est pas valide ou est n'est pas enregistrer. Merci de saisir un ID valide.")
        menu()
    else:   #sinon on propose de modifier le contenue et la nouvelle catégorie de la note cibler
        content = input("Saisissez le nouveau contenue de votre note: ")
        category = input("Quelle est la nouvelle catégorie de cette note ? : ")
        moddif = Note(content, category)

        curs.execute(""" UPDATE notes SET content = %s, category = %s WHERE id = %s;""", (moddif.content, moddif.category, id))
        #requête sql basique pour changer des valeurs dans une table
        conn.commit()
        #une fois que le code à fonctionner on envoie ce message pour prévenir l'utilisateur
        print("Bravo ! Votre note à été modifier avec succès!")
    menu()

def supr():
    id = input("Saisissez l'id de la note que vous voulez supprimer définitivement: ")
    curs.execute(""" SELECT id FROM notes WHERE id = %s;""", (id))
    n = curs.fetchone() #on reprend le code d'avant pour trouver id qui à été inscrit par l'user
    if n is None:
        print( #comme avant si l'id de la note n'existe pas on renvoie ce message d'erreur et on renvoie au menu
            "L'ID que vous venez d'entrer n'est pas valide ou n'est pas enregistrer. Merci de saisir un ID valide.")
        menu()
    else:   #sinon on supprime la note cibler
        curs.execute(""" DELETE FROM notes WHERE id = %s;""", (id))
        # requête sql basique pour supprimer des valeurs dans une table
        conn.commit()   #on envoie un message quand la note à bien été supprimer pour prévenir l'utilisateur
        print("La note que vous vouliez supprimer à été suporimer avec succès ! ")
    menu()
def menu(): #affiche le menu dans le terminal python, on choisi ce que l'ont veux utiliser
        print("Notre Menu :")
        print("1) Enregistrer une note: ")
        print("2) Afficher toute vos note: ")
        print("3) Saisissez l'id de la note que vous voulez voir: ")
        print("4) Saisissez l'id de la note à moddifer: ")
        print("5) Saisissez l'id de la note que vous voulez supprimer définitivement: ")
        print("6) Quitter le programme: ")
        choice = int(input("Quel option voulez vous utiliser ? "))
        if choice == 1: #enregistrement de la note nouvellement créer
            nouvellenote()
        if choice == 2: #voir toute les notes
            tout()
        if choice == 3: #choix de la note à voir
            selection()
        if choice == 4: #moddifier une note existante à partir de son id
            modif()
        if choice == 5: #supprimer une note existante à partir de son id
            supr()
        if choice == 6: #quiter le programme
            exit()
        else:   #si rien de présent dans les options est marquer alors on envoie ce message et on reviens au début du menu
            print("Merci de saisir une des options proposer ! ")
            menu()

#Arnaud Fischer
menu()