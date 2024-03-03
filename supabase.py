import supabase
from supabase import create_client, Client
 
url ="(url)"
key ="(key)"
supabase: Client = create_client(url, key)
class Note:
    def __init__(self, content, category):  #__init__ défini l'état initial des objets de la class
        # est aussi un constructeur qui initialise les attributs avant d'utiliser un / des objet(s)
        self.content = content
        self.category = category
def nouvellenote():
    content = input("Saisissez le contenue de votre note: ")   #on demande le contenu et la categorie que l'user veut pour sa note
    category = input("Saisissez la catégorie de cette note: ")
    response = supabase.table('notes') \
        .insert({"content": content, "category": category, }) \
        .execute()
    print("Bravo !! Votrre note à été créer avec succès!")
    menu()
def tout():
    affiche= supabase.table("notes").select("*").execute()
    print(affiche)
    menu()
def selection():
    id = input("Choissiez l'ID de la note que vous souhaitez afficher: ")
    response = supabase.table("notes").select("*").eq('id', id).execute()
    if response.data is None:
        print("La note séléctionner n'a pas été trouver")
    else:
        print(response.data[0])

def modif():
    id = input("Choissiez la note que vous voulez modifier: ")
    new_content = input("Nouveau contenue: ")
    new_category =input("Nouvelle catégorie: ")
    response = supabase.table("notes").update({"content": new_content, "category": new_category}).eq('id',id).execute()
    if response is None:
        print("Merci de saisir un id existant")
    else:
        print("Votre Note à bien été modiffier")
    menu()

def supr():
    id = input("Saisissez l'id de la note que vous voulez supprimer définitivement: ")
    response = supabase.table("notes").delete().eq('id', id).execute()
    if response is None:    #on verrfifie response
        print("Merci de saisir un id existant")
    else:
        print("Votre Note à bien été supprimer")
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
        else:   #si rien de présent dans les options marquer alors on envoie ce message et on reviens au début du menu
            print("Merci de saisir une des options proposer ! ")
            menu()

menu()
