import tkinter as tk
import random as rd


#Création des fenetres

fenetre = tk.Tk()
fenetre.geometry("1600x1000")  # Taille de la fenêtre
fenetre.configure(bg='#c0c0c0')

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

border_joueur_waiting_liste = [border_joueur_waiting_0, border_joueur_waiting_1, border_joueur_waiting_2, border_joueur_waiting_3, border_joueur_waiting_4, border_joueur_waiting_5]
border_taverne_liste = [border_taverne0 , border_taverne1 , border_taverne2]



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
        self.nom = "Murloc explorateur"
        self.pv = 5
        self.atq = 3
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_1.png")

class Murloc_type_2(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Murloc acrobate"
        self.pv = 5
        self.atq = 3
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_2.png")

class Paladin_type_1(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Guerrier sacré"
        self.pv = 5
        self.atq = 3
        self.tier = 1
        self.tribe = "Paladin"
        self.image = tk.PhotoImage(file="Images/Paladin_1.png")

class Bete_type_1(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "La bete sanguinaire"
        self.pv = 5
        self.atq = 3
        self.tier = 1
        self.tribe = "Bete"
        self.image = tk.PhotoImage(file="Images/Bete_1.png")


Liste_cartes_tier1 = [Murloc_type_1, Murloc_type_2, Paladin_type_1, Bete_type_1]
Liste_cartes_tier2 = Liste_cartes_tier1 + []

Liste_tier = [Liste_cartes_tier1 , Liste_cartes_tier2]

Liste_serviteurs = []

colors_taverne = [0,0,0]
colors_board = [0,0,0,0,0,0]

image_void = tk.PhotoImage(file="Images/void.png")
image_taverne = [image_void, image_void, image_void]
emplacement_taverne_libre = [0,0,0]    # 0 correspond à une place libre et 1 correspondra à une place occupée
image_board = [image_void, image_void, image_void, image_void, image_void, image_void]
emplacement_board_libre = [0,0,0,0,0,0]
image_terrain = [image_void, image_void, image_void, image_void]
emplacement_terrain_libre = [0,0,0,0]

#Texte :
Message_bienvenue = tk.Label(fenetre, text="Bienvenue dans la taverne!", font=("Calibri", 16), fg="red", bg='#c0c0c0')
Message_bienvenue.place(x=700, y=40)

Message_taverne = tk.Label(fenetre, text="Achetez ici vos serviteurs", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_taverne.place(x = 20, y = 150)
Message_taverne_fleche = tk.Label(fenetre, text="--->", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_taverne_fleche.place(x = 100, y = 180)

Message_terrain1 = tk.Label(fenetre, text="Placez ici vos serviteurs", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_terrain2 = tk.Label(fenetre, text="pour le combat", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_terrain_fleche = tk.Label(fenetre, text="--->", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_terrain1.place(x = 20, y = 480)
Message_terrain2.place(x = 50, y = 505)
Message_terrain_fleche.place(x = 100, y = 535)


def on_mouse_click(event):
    # Récupérer les coordonnées absolues de la souris
    abs_x, abs_y = event.widget.winfo_pointerxy()
    # Récupérer les coordonnées de la fenêtre Tkinter (obligatoire pour déplacer la fenêtre
    fenetre_x, fenetre_y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
    # Calculer les coordonnées relatives à la fenêtre Tkinter
    rel_x, rel_y = abs_x - fenetre_x, abs_y - fenetre_y

    #Pour changer la couleur du rectangle autour des cartes de la taverne
    if 235 < rel_x < 235 + 167 and 100 < rel_y < 100 + 260 and emplacement_taverne_libre[0] == 1:
        clic_sur_taverne(0)
    if 445 < rel_x < 445 + 167 and 100 < rel_y < 100 + 260 and emplacement_taverne_libre[1] == 1:
        clic_sur_taverne(1)
    if 655 < rel_x < 655 + 167 and 100 < rel_y < 100 + 260 and emplacement_taverne_libre[2] == 1:
        clic_sur_taverne(2)
    #Pour le déplacement d'une carte de la taverne vers la main du joueur
    if 25 < rel_x < 25 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[0] == 0:
        clic_sur_board_vide(25, 720, 0)
    if 235 < rel_x < 235 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[1] == 0:
        clic_sur_board_vide(235, 720, 1)
    if 445 < rel_x < 445 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[2] == 0:
        clic_sur_board_vide(445, 720, 2)
    if 655 < rel_x < 655 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[3] == 0:
        clic_sur_board_vide(655, 720, 3)
    if 865 < rel_x < 865 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[4] == 0:
        clic_sur_board_vide(865, 720, 4)
    if 1075 < rel_x < 1075 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[5] == 0:
        clic_sur_board_vide(1075, 720, 5)
    #Pour changer la couleur du rectangle autour des cartes du board
    if 25 < rel_x < 25 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[0] == 1:
        clic_sur_board_occupe(0)
    if 235 < rel_x < 235 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[1] == 1:
        clic_sur_board_occupe(1)
    if 445 < rel_x < 445 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[2] == 1:
        clic_sur_board_occupe(2)
    if 655 < rel_x < 655 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[3] == 1:
        clic_sur_board_occupe(3)
    if 865 < rel_x < 865 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[4] == 1:
        clic_sur_board_occupe(4)
    if 1075 < rel_x < 1075 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[5] == 1:
        clic_sur_board_occupe(5)

def clic_sur_taverne(colors_index):
    global colors_taverne
    if colors_taverne[colors_index] == 0:
        colors_taverne = [0,0,0]
        colors_taverne[colors_index] = 1
    else:
        colors_taverne[colors_index] = 0
    for i in range (3):
        if colors_taverne[i] == 0:
            canvas.itemconfigure(border_taverne_liste[i], outline='blue')
        if colors_taverne[i] == 1:
            canvas.itemconfigure(border_taverne_liste[i], outline='red')

def clic_sur_board_vide(x,y, indice_board):
    global colors_taverne, emplacement_taverne_libre, colors_board
    for i in range(3):
        if colors_taverne[i] == 1:
            canvas.coords(image_taverne[i], x, y)
            image_board[indice_board] = image_taverne[i]
            image_taverne[i] = canvas.create_image(235 + i*210, 100, anchor=tk.NW, image=image_void)
            colors_taverne[i] = 0
            canvas.itemconfigure(border_taverne_liste[i], outline='blue')
            emplacement_taverne_libre[i] = 0
            emplacement_board_libre[indice_board] = 1
            colors_board[indice_board] = 1 #Il est necessaire de changer la couleur de la bordure vu l'ordre des évènements

#def poser_un_serviteur(x,y, indice_terrain):


def clic_sur_board_occupe(colors_index):
    global colors_board
    if colors_board[colors_index] == 0:
        colors_board = [0,0,0,0,0,0]
        colors_board[colors_index] = 1
    else:
        colors_board[colors_index] = 0
    for i in range (6):
        if colors_board[i] == 0:
            canvas.itemconfigure(border_joueur_waiting_liste[i], outline='blue')
        if colors_board[i] == 1:
            canvas.itemconfigure(border_joueur_waiting_liste[i], outline='red')



def remplissage_taverne(tier):
    global Liste_serviteurs, emplacement_taverne_libre
    nb_cartes = len(Liste_tier[tier-1])
    for i in range(3):
        nb_aléatoire = rd.randint(0, nb_cartes-1)
        id_serviteur = len(Liste_serviteurs)
        Liste_serviteurs = Liste_serviteurs + [0]

        if nb_aléatoire == 0:
            Liste_serviteurs[id_serviteur] = Murloc_type_1(id_serviteur)
        if nb_aléatoire == 1:
            Liste_serviteurs[id_serviteur] = Murloc_type_2(id_serviteur)
        if nb_aléatoire == 2:
            Liste_serviteurs[id_serviteur] = Paladin_type_1(id_serviteur)
        if nb_aléatoire == 3:
            Liste_serviteurs[id_serviteur] = Bete_type_1(id_serviteur)

        image_taverne[i] = canvas.create_image(235 + i*210, 100, anchor=tk.NW, image=Liste_serviteurs[id_serviteur].image)
        emplacement_taverne_libre[i] = 1



def initialisation_board_et_terrain():
    for i in range (6):
        image_board[i] = canvas.create_image(25 + 210 * i, 720, anchor=tk.NW, image=image_void)
    for i in range(4):
        image_terrain[i] = canvas.create_image(235 + 210 * i, 420, anchor=tk.NW, image=image_void)







initialisation_board_et_terrain()


remplissage_taverne(1)


fenetre.bind("<Button-1>", on_mouse_click)
fenetre.mainloop()


