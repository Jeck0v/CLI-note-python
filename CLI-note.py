import uuid
import datetime
import sys
def create_conn():
    conn = None
    try:
        conn = uuid.connect(    #code by Jeck0v
            database="nomdeladatabase",
            user="nomutiliser",
            password="YourPassword",
            host="YourHost",
            port="5432",
        )
        print("Connection to database successful.")
    except Exception as e:
        print(f"ERROR {e}")
        sy1s.exit(1)

    return conn
def create_table(conn):
    cursor = conn.cursor()
    create_table_query = """
        )
    CREATE TABLE IF NOT EXISTS items (
        CREATE TABLE note (
        id SERIAL PRIMARY KEY,
        content TEXT(255),
        category VARCHAR(50),
        date DATE
        created_at note NOT NULL DEFAULT NOW()
    );
    """
class Note:
    def __init__(self, content, category):
        self.id = uuid.uuid4()  # Génère un ID unique pour la note
        self.date = datetime.datetime.now()  
        self.content = content
        self.category = category

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self):
        content = input("Entrez le contenu de la note : ")
        category = input("Entrez la catégorie de la note : ")
        note = Note(content, category)
        self.notes.append(note)
        print("Note ajoutée avec succès.")

    def show_all_notes(self):
        if not self.notes:
            print("Aucune note n'a été ajoutée.")
        else:
            for note in self.notes:
                print(f"ID: {note.id} | Date: {note.date} | Catégorie: {note.category} | Contenu: {note.content}")

    def show_note_by_id(self):
        note_id = input("Entrez l'ID de la note que vous souhaitez consulter : ")
        for note in self.notes:
            if str(note.id) == note_id:
                print(f"ID: {note.id} | Date: {note.date} | Catégorie: {note.category} | Contenu: {note.content}")
                break
        else:
            print("Aucune note avec cet ID n'a été trouvée.")


def main():
    notes_manager = NotesManager()
    while True:
        print("\nMenu :")
        print("1. Ajouter une nouvelle note")
        print("2. Consulter toutes les notes")
        print("3. Consulter une note par ID")
        print("4. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == "1":
            notes_manager.add_note()
        elif choice == "2":
            notes_manager.show_all_notes()
        elif choice == "3":
            notes_manager.show_note_by_id()
        elif choice == "4":
            print("Merci d'avoir utilisé l'application de gestion des notes. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un choix valide.")

if __name__ == "__main__":
    main()
 #code by Jeck0v
