import tkinter as tk
import random as rd


#Création des fenetres

fenetre = tk.Tk()
fenetre.geometry("1600x1000")  # Taille de la fenêtre

canvas = tk.Canvas(fenetre, width=1600, height=1000)
canvas.pack()
canvas.configure(bg='#c0c0c0')      # Couleur gris clair



# Création des bordures d'images pour les interfaces :
border_joueur_waiting_0 = canvas.create_rectangle(25, 720, 25 + 167, 720 + 260, outline='blue', width=5)
border_joueur_waiting_1 = canvas.create_rectangle(235, 720, 235 + 167, 720 + 260, outline='blue', width=5)
border_joueur_waiting_2 = canvas.create_rectangle(445, 720, 445 + 167, 720 + 260, outline='blue', width=5)
border_joueur_waiting_3 = canvas.create_rectangle(655, 720, 655 + 167, 720 + 260, outline='blue', width=5)
border_joueur_waiting_4 = canvas.create_rectangle(865, 720, 865 + 167, 720 + 260, outline='blue', width=5)
border_joueur_waiting_5 = canvas.create_rectangle(1075, 720, 1075 + 167, 720 + 260, outline='blue', width=5)

border_battler_on_field_0 = canvas.create_rectangle(235, 420, 235 + 167, 420 + 260, outline='blue', width=5)
border_battler_on_field_1 = canvas.create_rectangle(445, 420, 445 + 167, 420 + 260, outline='blue', width=5)
border_battler_on_field_2 = canvas.create_rectangle(655, 420, 655 + 167, 420 + 260, outline='blue', width=5)
border_battler_on_field_3 = canvas.create_rectangle(865, 420, 865 + 167, 420 + 260, outline='blue', width=5)

border_taverne0 = canvas.create_rectangle(235, 100, 235 + 167, 100 + 260, outline='blue', width=5)
border_taverne1 = canvas.create_rectangle(445, 100, 445 + 167, 100 + 260, outline='blue', width=5)
border_taverne2 = canvas.create_rectangle(655, 100, 655 + 167, 100 + 260, outline='blue', width=5)

#



class Serviteur:
    def __init__(self, id_serviteur):
        self.nom = ""
        self.pv = 0
        self.atq = 0
        self.tier = 0
        self.image = None
        self.id_serviteur = id_serviteur

    def attaquer(self, opposant):
        opposant.pv = opposant.pv - self.atq
        self.pv = self.pv - opposant.atq
        a = 0
        if (self.pv <= 0):
            a = a + 1  # La variable a permet de savoir si des combattants sont morts pendant l'attaque, si battler1 est mort a = 1, si battler 2 est mort a = 2 et si les deux sont morts a =3
        if (opposant.pv <= 0):
            a = a + 2
        return a


#Serviteurs
class Murloc_type_1(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Murloc1"
        self.pv = 5
        self.atq = 3
        self.tier = 1
        self.image = tk.PhotoImage(file="Images/Murloc_1.png")

class Murloc_type_2(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Murloc2"
        self.pv = 5
        self.atq = 3
        self.tier = 1
        self.image = tk.PhotoImage(file="Images/Murloc_2.png")


Liste_cartes_tier1 = [Murloc_type_1, Murloc_type_2]
Liste_cartes_tier2 = Liste_cartes_tier1 + []

Liste_tier = [Liste_cartes_tier1 , Liste_cartes_tier2]

Liste_serviteurs = []

image_void = tk.PhotoImage(file="Images/void.png")
image_taverne = [image_void, image_void, image_void]
image_board = [image_void, image_void, image_void, image_void, image_void, image_void]



def on_mouse_click(event):
    # Récupérer les coordonnées absolues de la souris
    abs_x, abs_y = event.widget.winfo_pointerxy()
    # Récupérer les coordonnées de la fenêtre Tkinter (obligatoire pour déplacer la fenêtre
    fenetre_x, fenetre_y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
    # Calculer les coordonnées relatives à la fenêtre Tkinter
    rel_x, rel_y = abs_x - fenetre_x, abs_y - fenetre_y
    # afficher les coordonnées
    print("Mouse clicked at x =", rel_x, " y =", rel_y)

def remplissage_taverne(tier):
    global Liste_serviteurs
    nb_cartes = len(Liste_tier[tier-1])
    for i in range(3):
        nb_aléatoire = rd.randint(0, nb_cartes-1)
        id_serviteur = len(Liste_serviteurs)
        Liste_serviteurs = Liste_serviteurs + [0]

        if nb_aléatoire == 0:
            Liste_serviteurs[id_serviteur] = Murloc_type_1(id_serviteur)
        if nb_aléatoire == 1:
            Liste_serviteurs[id_serviteur] = Murloc_type_2(id_serviteur)

        image_taverne[i] = canvas.create_image(235 + i*210, 100, anchor=tk.NW, image=Liste_serviteurs[id_serviteur].image)


def initialisation_board():
    for i in range (6):
        image_board[i] = canvas.create_image(25 + 210 * i, 720, anchor=tk.NW, image=image_void)







initialisation_board()


remplissage_taverne(1)



fenetre.bind("<Button-1>", on_mouse_click)
fenetre.mainloop()


