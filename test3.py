from tkinter import *

# Création de la fenêtre principale
root = Tk()

# Création du canvas
canvas = Canvas(root, width=200, height=100)
canvas.pack()

# Création du rectangle vide
rectangle_id = canvas.create_rectangle(10, 10, 50, 50, fill='#ffffff00')

# Création de la fonction de callback
def rectangle_clicked(event):
    print("Rectangle clicked at", event.x, event.y)

# Liaison de la fonction de callback à l'événement de souris "clic" sur le rectangle
canvas.tag_bind(rectangle_id, "<Button-1>", rectangle_clicked)

root.mainloop()