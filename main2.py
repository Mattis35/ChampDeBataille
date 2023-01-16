import tkinter as tk
import random as rd
import time


fenetre = tk.Tk()
fenetre.geometry("1600x1000")  # Taille de la fenêtre
fenetre.configure(bg='#c0c0c0')

# Configuration des canvas

canvas_taverne = tk.Canvas(fenetre, width=1600, height=1000)    #Canvas utilisé pour l'interface taverne
canvas_taverne.pack()   # Permet d'ajouter le canvas à la fenetre principale
canvas_taverne.configure(bg='#c0c0c0')      # Couleur gris clair
canvas_taverne.grid()

canvas_combat = tk.Canvas(fenetre, width=1600, height=1000)     #Canvas utilisé pour l'interface combat
canvas_combat.configure(bg='#c0c0c0')


image_void = tk.PhotoImage(file="Images/void.png")


class Player:
    def __init__(self, nom):
        self.nom = nom
        self.hp = 20
        self.gold = 100
        self.taverne_tier = 3
        self.serviteurs_au_combat = [0,0,0,0]
        self.next_battler = 0      #Utile en combat

class Serviteur:
    def __init__(self):
        self.nom = ""
        self.pv = 0
        self.atq = 0
        self.tier = 0
        self.image = None

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
    def __init__(self):
        super().__init__()
        self.nom = "Murloc explorateur"
        self.pv = 1
        self.atq = 1
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_1.png")

class Murloc_type_2(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Murloc acrobate"
        self.pv = 3
        self.atq = 1
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_2.png")

class Murloc_type_3(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Murloc ecuyer"
        self.pv = 4
        self.atq = 4
        self.tier = 2
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_3.png")

class Murloc_type_4(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Le sage vert"
        self.pv = 6
        self.atq = 6
        self.tier = 3
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_4.png")

class Paladin_type_1(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Guerrier sacré"
        self.pv = 3
        self.atq = 1
        self.tier = 1
        self.tribe = "Paladin"
        self.image = tk.PhotoImage(file="Images/Paladin_1.png")

class Bete_type_1(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "La bete sanguinaire"
        self.pv = 4
        self.atq = 2
        self.tier = 1
        self.tribe = "Bete"
        self.image = tk.PhotoImage(file="Images/Bete_1.png")


Liste_cartes_tier1 = [Murloc_type_1, Murloc_type_2, Paladin_type_1, Bete_type_1]
Liste_cartes_tier2 = Liste_cartes_tier1 + [Murloc_type_3]
Liste_cartes_tier3 = Liste_cartes_tier2 + [Murloc_type_4]

Liste_tier = [Liste_cartes_tier1 , Liste_cartes_tier2, Liste_cartes_tier3]



class Tile:
    def __init__(self, nom, canvas, x, y):
        self.nom = nom
        self.x = x  # Coordonnées du coin en haut à gauche de l'emplacement
        self.y = y
        self.largeur = 167
        self.longueur = 260
        self.image = image_void
        self.atq_x = x + 25
        self.hp_x = x + 130
        self.atq_y = y + 166
        self.hp_y = y + 166
        self.color = "black"
        self.canvas = canvas    # Permet de savoir sur quel canvas se situe l'objet
        self.serviteur = 0  #Permet de savoir quel serviteur est sur la tuile, vaut 0 si il n'y a pas de serviteur
        self.border = self.canvas.create_rectangle(x, y, x + self.largeur, y + self.longueur, outline=self.color, width=5)
        self.image_posée = self.canvas.create_image(x, y, anchor=tk.NW, image=self.image)


    def update_bordure(self):
        self.canvas.itemconfigure(self.border, outline=self.color)

    def update_image(self):
        # On supprime l'image affichée précédemment
        self.canvas.delete(self.image_posée)

        #Si un serviteur est posé sur cette tuile, l'image de la tuile est l'image du serviteur
        if self.serviteur != 0:
            self.image = self.serviteur.image
        #Sinon l'image est l'image du vide
        else :
            self.image = image_void
        self.image_posée = self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.image)

    def update(self):
        self.update_bordure()
        self.update_image()



# Création des 3 listes dans les quels nous allons placer nos objets de type Tiles
Tiles_taverne = []  # Liste de 3
Tiles_main = []     # Liste de 6
Tiles_plateau = []  # Liste de 4

# Remplissage des 3 listes
for i in range (3):
    Tiles_taverne = Tiles_taverne + [Tile("Taverne" + str(i), canvas_taverne, 235 + 210 * i,100)]
for i in range (6):
    Tiles_main = Tiles_main + [Tile("Main" + str(i), canvas_taverne, 25 + 210 * i, 720)]
for i in range (4):
    Tiles_plateau = Tiles_plateau + [Tile("Plateau" + str(i), canvas_taverne, 235 + 210 * i,420)]

# Création d'une liste regroupant les 3 listes précédentes pour que cela soit + pratique
Tiles_total_taverne = Tiles_taverne + Tiles_main + Tiles_plateau # Liste de 13


# Variables globales

lieu = "taverne" # Permet de savoir si l'on se trouve à la taverne ou au combat


# Fonctions

def on_mouse_click(event):
    global lieu

    # Récupérer les coordonnées absolues de la souris
    abs_x, abs_y = event.widget.winfo_pointerxy()
    # Récupérer les coordonnées de la fenêtre Tkinter (obligatoire pour déplacer la fenêtre
    fenetre_x, fenetre_y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
    # Calculer les coordonnées relatives à la fenêtre Tkinter
    rel_x, rel_y = abs_x - fenetre_x, abs_y - fenetre_y

    if lieu == "taverne":

        for i in range(13):
            if Tiles_total_taverne[i].x < rel_x < Tiles_total_taverne[i].x + Tiles_total_taverne[i].largeur and Tiles_total_taverne[i].y < rel_y < Tiles_total_taverne[i].y + Tiles_total_taverne[i].longueur and Tiles_total_taverne[i].image != image_void:
                clic_sur_carte(i)
        for i in range(6):
            if Tiles_main[i].x < rel_x < Tiles_main[i].x + Tiles_main[i].largeur and Tiles_main[i].y < rel_y < Tiles_main[i].y + Tiles_main[i].longueur and Tiles_main[i].image == image_void:
                clic_sur_main_vide(i)



def remplissage_taverne(tier):
    nb_cartes = len(Liste_tier[tier-1])
    for i in range(3):
        nb_aléatoire = rd.randint(0, nb_cartes-1)

        Tiles_taverne[i].serviteur = Liste_tier[tier-1][nb_aléatoire]()
        Tiles_taverne[i].update_image()

def clic_sur_carte(indice):
    a = "black"
    if Tiles_total_taverne[indice].color == "black":
        a = "red"
    for i in range(13):
        Tiles_total_taverne[i].color = "black"
        Tiles_total_taverne[i].update_bordure()
    Tiles_total_taverne[indice].color = a
    Tiles_total_taverne[indice].update_bordure()



def clic_sur_main_vide(indice):
    for i in range(3):
        if Tiles_taverne[i].color == "red":
            if Joueur.gold >= 3:
                Tiles_taverne[i].color = "black"
                Tiles_main[indice].serviteur = Tiles_taverne[i].serviteur
                Tiles_taverne[i].serviteur = 0
                Tiles_main[indice].update()
                Tiles_taverne[i].update()

            else : print("You need to have 3 gold to buy a card")




#Tests
Joueur = Player("Mattis")

remplissage_taverne(Joueur.taverne_tier)


fenetre.bind("<Button-1>", on_mouse_click)
fenetre.mainloop()
