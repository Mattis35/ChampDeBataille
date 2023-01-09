#import tkinter as tk
"""
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Crée un objet PhotoImage à partir de l'image souhaitée
        self.image = tk.PhotoImage(file="Images/Murloc_1.png")

        # Crée un widget Label avec l'image
        self.label = tk.Label(self, image=self.image)

        # Place le widget dans la fenêtre
        self.label.pack()

        # Crée un booléen pour suivre l'état du glisser-déposer
        self.dragging = False

        # Crée des variables pour suivre la position de la souris pendant le glisser-déposer
        self.drag_x = 0
        self.drag_y = 0

        # Associe les évènements aux fonctions de gestion du glisser-déposer
        self.label.bind("<ButtonPress-1>", self.on_drag_start)
        self.label.bind("<ButtonRelease-1>", self.on_drag_stop)
        self.label.bind("<Motion>", self.on_drag_move)

        # Crée un widget Frame pour servir de zone de dépôt
        self.drop_zone = tk.Frame(self, bg="lightblue", width=200, height=200)

        # Place la zone de dépôt en bas à droite de la fenêtre
        self.drop_zone.pack(side=tk.BOTTOM, anchor=tk.E)

    def on_drag_start(self, event):
        # Démarre le glisser-déposer en enregistrant la position de la souris
        self.dragging = True
        self.drag_x = event.x
        self.drag_y = event.y

    def on_drag_stop(self, event):
        # Termine le glisser-déposer en remettant le booléen à False
        self.dragging = False

        # Si l'image est déposée dans la zone de dépôt, change la couleur de fond de la zone
        if self.label.winfo_containing(event.x_root, event.y_root) == self.drop_zone:
            self.drop_zone.config(bg="green")

    def on_drag_move(self, event):
        # Si le glisser-déposer est en cours, déplace le widget en fonction de la position de la souris
        if self.dragging:
            x = self.winfo_x() + event.x - self.drag_x
            y = self.winfo_y() + event.y - self.drag_y
            self.label.place(x=x, y=y)

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()



"""
import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("1000x1000")  # Taille de la fenêtre

# Création du Canvas
canvas = tk.Canvas(fenetre, width=1000, height=1000)
canvas.pack()

# Chargement de l'image
image = tk.PhotoImage(file="Images/Murloc_2.png")

# Création de l'objet image sur le canvas
image_on_canvas = canvas.create_image(50, 50, anchor=tk.NW, image=image)

# Création de la bordure de l'image
border_id = canvas.create_rectangle(50, 50, 50 + image.width(), 50 + image.height(), outline='blue', width=5)
color = 1

# Placement de la bordure derrière l'image
canvas.lower(border_id, image_on_canvas)

# Fonction appelée lorsque l'on clique sur l'image
def clic_sur_image(event):
    # Changement de la couleur de la bordure
    canvas.itemconfigure(border_id, outline='red')


# Attribution de la fonction "clic_sur_image" comme gestionnaire d'évènement "clic" pour l'image
canvas.tag_bind(image_on_canvas, "<Button-1>", clic_sur_image)

# Affichage de la fenêtre
fenetre.mainloop()


#Images/Murloc_1.png



