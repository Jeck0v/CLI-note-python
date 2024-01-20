
import psycopg2
import tkinter as tk
from tkinter import messagebox

conn = psycopg2.connect(
    database="notes",        #Si vous changez le nom, n'oublier pas de le modifier partout
    user="(user name)",
    password="(password)",
    host="localhost",
    port="5432"
)
curs = conn.cursor()
window = tk.Tk()
class Note:
    def __init__(self, content, category):
        self.content = content
        self.category = category

def create_note(content, category):
    new = Note(content, category)
    curs.execute("""
        INSERT INTO notes (content, category)
        VALUES(%s, %s);
    """, (new.content, new.category))
    conn.commit()

def read_notes():
    curs.execute("""
        SELECT * FROM notes;
    """)
    notes = curs.fetchall()
    return notes

def read_note(note_id):
    curs.execute("""
        SELECT * FROM notes WHERE id = %s;
    """, (note_id,))
    note = curs.fetchone()
    return note

def update_note(note_id, content, category):
    curs.execute("""
        UPDATE notes SET content = %s, category = %s WHERE id = %s;
    """, (content, category, note_id))
    conn.commit()

def delete_note(note_id):
    curs.execute("""
        DELETE FROM notes WHERE id = %s;
    """, (note_id,))
    conn.commit()

def main_window():
    window = tk.Tk()
    window.title("To-Do List")

def create_note_command():
        content = content_entry.get()
        category = category_entry.get()
        if content and category:
            create_note(content, category)
            messagebox.showinfo("Note Créer", "La note à bien été créer")
            content_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erreur", "Merci, d'entrer un contenu et une catégorie complète")

def view_all_notes_command():
        notes = read_notes()
        note_listbox.delete(0, tk.END)
        for note in notes:
            note_listbox.insert(tk.END, note)

def view_note_command():
        note_id = note_id_entry.get()
        note = read_note(note_id)
        if note:
            note_listbox.delete(0, tk.END)
            note_listbox.insert(tk.END, note)
        else:
            messagebox.showerror("Erreur", "L'id choisi n'existe pas")

def edit_note_command():
        note_id = note_id_entry.get()
        content = content_entry.get()
        category = category_entry.get()
        if content and category:
            update_note(note_id, content, category)
            messagebox.showinfo("Note mise à jour", "La note a bien été mise à jour")
            view_all_notes_command()
        else:
            messagebox.showerror("Erreur", "Merci, d'entrer un contenu et une catégorie complète")

def delete_note_command():
        note_id = note_id_entry.get()
        delete_note(note_id)
        messagebox.showinfo("Note supprimer", "La note a été supprimer avec succès")
        view_all_notes_command()


content_label = tk.Label(window, text="Contenu:")
content_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
content_entry = tk.Entry(window, width=50)
content_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

category_label = tk.Label(window, text="Categorie:")
category_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
category_entry = tk.Entry(window, width=50)
category_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

create_button = tk.Button(window, text="Crée une Note", command=create_note_command)
create_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

view_all_button = tk.Button(window, text="Voir toutes les notes", command=view_all_notes_command)
view_all_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

note_id_label = tk.Label(window, text="Note ID:")
note_id_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
note_id_entry = tk.Entry(window, width=10)
note_id_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

view_button = tk.Button(window, text="Voir la Note", command=view_note_command)
view_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

edit_button = tk.Button(window, text="Modifier une Note", command=edit_note_command)
edit_button.grid(row=5, column=1, padx=10, pady=10, sticky="w")

delete_button = tk.Button(window, text="Supprimer une Note", command=delete_note_command)
delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

note_listbox = tk.Listbox(window, width=80, height=20)
note_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
window.mainloop()
