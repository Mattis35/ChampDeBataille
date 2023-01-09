import tkinter as tk
import random as rd

# Faire une liste des images ailleurs qui coincide avec la liste des id

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("1600x1000")  # Taille de la fenêtre

# Création du Canvas
canvas = tk.Canvas(fenetre, width=1600, height=1000)
canvas.pack()
canvas.configure(bg='#c0c0c0')  # Couleur gris clair


class Player:
    def __init__(self, nom):
        self.nom = nom
        self.hp = 20
        self.battlers_on_field = ["void", "void", "void", "void"]
        self.battlers_waiting = []

        self.gold = 3
        self.niveau = 1
        self.battlers_on_market = ["void", "void", "void"]


class Battler:
    def __init__(self, nom, pv, attaque, tier):
        self.nom = nom
        self.pv = pv
        self.atq = attaque
        self.tier = tier

    def attaquer(self, opposant):
        opposant.pv = opposant.pv - self.atq
        self.pv = self.pv - opposant.atq
        a = 0
        if (self.pv <= 0):
            a = a + 1  # La variable a permet de savoir si des combattants sont morts pendant l'attaque, si battler1 est mort a = 1, si battler 2 est mort a = 2 et si les deux sont morts a =3
        if (opposant.pv <= 0):
            a = a + 2
        return a


# Tribes :

class Murloc(Battler):
    def __init__(self, nom, pv, attaque, tier):
        super().__init__(nom, pv, attaque, tier)
        self.tribe = "Murloc"


class Paladin(Battler):
    def __init__(self, nom, pv, attaque, tier):
        super().__init__(nom, pv, attaque, tier)
        self.tribe = "Paladin"


class Bete(Battler):
    def __init__(self, nom, pv, attaque, tier):
        super().__init__(nom, pv, attaque, tier)
        self.tribe = "Bete"


# Cards :

class Murloc_type_1(Murloc):
    def __init__(self):
        super().__init__("Murloc explorateur", 3, 1, 1)
        self.tribe = self.tribe


class Murloc_type_2(Murloc):
    def __init__(self):
        super().__init__("Murloc acrobate", 4, 2, 2)
        self.tribe = self.tribe


class Paladin_type_1(Paladin):
    def __init__(self):
        super().__init__("Guerriers sacrés", 3, 1, 1)
        self.tribe = self.tribe


class Bete_type_1(Bete):
    def __init__(self):
        super().__init__("La Bete sanguinaire", 3, 1, 1)
        self.tribe = self.tribe


Liste_cartes_tier1 = [Murloc_type_1, Murloc_type_2, Paladin_type_1, Bete_type_1]
Liste_cartes_tier2 = Liste_cartes_tier1 + []

Liste_tier = [Liste_cartes_tier1, Liste_cartes_tier2]

# Chargement de toutes les images
Liste_images = [tk.PhotoImage(file="Images/Murloc_1.png"), tk.PhotoImage(file="Images/Murloc_2.png"),
                tk.PhotoImage(file="Images/Paladin_1.png"), tk.PhotoImage(file="Images/Bete_1.png")]

# Chargement de l'image void
image_void = tk.PhotoImage(file="Images/void.png")
image_taverne = [image_void, image_void, image_void]
image_board = [image_void, image_void, image_void, image_void, image_void, image_void]


def initialisation_board():
    for i in range(6):
        image_board[i] = canvas.create_image(25 + 210 * i, 720, anchor=tk.NW, image=image_void)


def remplissage_taverne(tier):
    nb_cartes = len(Liste_tier[tier - 1])
    for i in range(3):
        nb_aléatoire = rd.randint(0, nb_cartes - 1)
        image_taverne[i] = canvas.create_image(235 + i * 210, 100, anchor=tk.NW, image=Liste_images[nb_aléatoire])


initialisation_board()
remplissage_taverne(1)

# Création des bordures d'images pour les interfaces de taverne :
border_id_joueur_waiting_0 = canvas.create_rectangle(25, 720, 25 + 167, 720 + 260, outline='blue', width=5)
border_id_joueur_waiting_1 = canvas.create_rectangle(235, 720, 235 + 167, 720 + 260, outline='blue', width=5)
border_id_joueur_waiting_2 = canvas.create_rectangle(445, 720, 445 + 167, 720 + 260, outline='blue', width=5)
border_id_joueur_waiting_3 = canvas.create_rectangle(655, 720, 655 + 167, 720 + 260, outline='blue', width=5)
border_id_joueur_waiting_4 = canvas.create_rectangle(865, 720, 865 + 167, 720 + 260, outline='blue', width=5)
border_id_joueur_waiting_5 = canvas.create_rectangle(1075, 720, 1075 + 167, 720 + 260, outline='blue', width=5)

border_id_battler_on_field_0 = canvas.create_rectangle(235, 420, 235 + 167, 420 + 260, outline='blue', width=5)
border_id_battler_on_field_1 = canvas.create_rectangle(445, 420, 445 + 167, 420 + 260, outline='blue', width=5)
border_id_battler_on_field_2 = canvas.create_rectangle(655, 420, 655 + 167, 420 + 260, outline='blue', width=5)
border_id_battler_on_field_3 = canvas.create_rectangle(865, 420, 865 + 167, 420 + 260, outline='blue', width=5)

border_id_taverne0 = canvas.create_rectangle(235, 100, 235 + 167, 100 + 260, outline='blue', width=5)
border_id_taverne1 = canvas.create_rectangle(445, 100, 445 + 167, 100 + 260, outline='blue', width=5)
border_id_taverne2 = canvas.create_rectangle(655, 100, 655 + 167, 100 + 260, outline='blue', width=5)

border_id_joueur_waiting_liste = [border_id_joueur_waiting_0, border_id_joueur_waiting_1, border_id_joueur_waiting_2,
                                  border_id_joueur_waiting_3, border_id_joueur_waiting_4, border_id_joueur_waiting_5]
border_id_taverne_liste = [border_id_taverne0, border_id_taverne1, border_id_taverne2]

colors_taverne = [0, 0, 0]


# Fonction appelée lorsque l'on clique sur l'image
def clic_sur_taverne(event, colors_index):
    global colors_taverne
    if colors_taverne[colors_index] == 0:
        colors_taverne = [0, 0, 0]
        colors_taverne[colors_index] = 1
    else:
        colors_taverne[colors_index] = 0
    for i in range(3):
        if colors_taverne[i] == 0:
            canvas.itemconfigure(border_id_taverne_liste[i], outline='blue')
        if colors_taverne[i] == 1:
            canvas.itemconfigure(border_id_taverne_liste[i], outline='red')


canvas.tag_bind(border_id_taverne_liste[0], "<Button-1>", lambda event: clic_sur_taverne(event, 0))
canvas.tag_bind(border_id_taverne_liste[1], "<Button-1>", lambda event: clic_sur_taverne(event, 1))
canvas.tag_bind(border_id_taverne_liste[2], "<Button-1>", lambda event: clic_sur_taverne(event, 2))


def clic_sur_image_board(event, x, y, indice_board):
    global colors_taverne
    for i in range(3):
        if colors_taverne[i] == 1:
            canvas.coords(image_taverne[i], x, y)
            image_board[indice_board] = image_taverne[i]
            image_taverne[i] = canvas.create_image(235 + i * 210, 100, anchor=tk.NW, image=image_void)
            colors_taverne[i] = 0
            canvas.coords(border_id_taverne_liste[i], x, y, x + 167, y + 260)
            border_id_joueur_waiting_liste[indice_board] = border_id_taverne_liste[i]
            border_id_taverne_liste[i] = canvas.create_rectangle(235 + 210 * i, 100, 235 + 210 * i + 167, 100 + 260,
                                                                 outline='blue', width=5)


canvas.tag_bind(image_board[0], "<Button-1>", lambda event: clic_sur_image_board(event, 25, 720, 0))

# Affichage de la fenêtre
fenetre.mainloop()

# Images/Murloc_1.png


"""
# Création de combattants
murloc_1 = Murloc_type_1()
murloc_2 = Murloc_type_1()

# Combat
murloc_1.attaquer(murloc_2)

# Affichage de l'état des combattants après le combat
print(f"{murloc_1.nom} a {murloc_1.pv} PV")
print(f"{murloc_2.nom} a {murloc_2.pv} PV")
"""


# def Combat(p1, p2):


def Bataille(p1, p2):
    next_attacker = rd.randint(1,
                               2)  # Défini si c'est le joueur 1 qui commence à attaquer ou si c'est le 2ème. De plus, cette variable sera mise à jour à chaque attaque.
    p1_next_battler = 0
    p2_next_battler = 0

    while (p1.battlers_on_field != ["void", "void", "void", "void"] or p2.battlers_on_field != ["void", "void", "void",
                                                                                                "void"]):
        next_attacker = 1  #
        if (next_attacker == 1):

            while (p1.battlers_on_field[p1_next_battler] == "void"):
                p1_next_battler += 1
                if (p1_next_battler == 4):
                    p1_next_battler = 0

            target = rd.randint(0, 3)
            while (p2.battlers_on_field[target] == "void"):
                target = rd.randint(0, 3)

            a = p1.battlers_on_field[p1_next_battler].attaquer(p2.battlers_on_field[target])
            if (a == 1 or a == 3):
                p1.battlers_on_field[p1_next_battler] = "void"
            if (a == 2 or a == 3):
                p2.battlers_on_field[p1_next_battler] = "void"
            p1_next_battler += 1


Moi = Player("Moi")
Ennemy = Player("Ennemy")

Moi.battlers_on_field[0] = Murloc_type_1()
Ennemy.battlers_on_field[0] = Murloc_type_1()

murloc_1 = Murloc_type_1()

# print(Moi.battlers_on_field)

Bataille(Moi, Ennemy)

