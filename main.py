import tkinter as tk
import random as rd
import time


#Création de la fenetres et des 2 canvas

fenetre = tk.Tk()
fenetre.geometry("1600x1000")  # Taille de la fenêtre
fenetre.configure(bg='#c0c0c0')

canvas = tk.Canvas(fenetre, width=1600, height=1000)    #Canvas utilisé pour l'interface taverne
canvas.pack()
canvas.configure(bg='#c0c0c0')      # Couleur gris clair
canvas.grid()

canvas_combat = tk.Canvas(fenetre, width=1600, height=1000)     #Canvas utilisé pour l'interface combat
canvas_combat.configure(bg='#c0c0c0')


# Création des bordures d'images pour les interfaces :
border_joueur_waiting_0 = canvas.create_rectangle(25, 720, 25 + 167, 720 + 260, outline='black', width=5)
border_joueur_waiting_1 = canvas.create_rectangle(235, 720, 235 + 167, 720 + 260, outline='black', width=5)
border_joueur_waiting_2 = canvas.create_rectangle(445, 720, 445 + 167, 720 + 260, outline='black', width=5)
border_joueur_waiting_3 = canvas.create_rectangle(655, 720, 655 + 167, 720 + 260, outline='black', width=5)
border_joueur_waiting_4 = canvas.create_rectangle(865, 720, 865 + 167, 720 + 260, outline='black', width=5)
border_joueur_waiting_5 = canvas.create_rectangle(1075, 720, 1075 + 167, 720 + 260, outline='black', width=5)

border_battler_on_field_0 = canvas.create_rectangle(235, 420, 235 + 167, 420 + 260, outline='black', width=5)
border_battler_on_field_1 = canvas.create_rectangle(445, 420, 445 + 167, 420 + 260, outline='black', width=5)
border_battler_on_field_2 = canvas.create_rectangle(655, 420, 655 + 167, 420 + 260, outline='black', width=5)
border_battler_on_field_3 = canvas.create_rectangle(865, 420, 865 + 167, 420 + 260, outline='black', width=5)

border_taverne0 = canvas.create_rectangle(235, 100, 235 + 167, 100 + 260, outline='black', width=5)
border_taverne1 = canvas.create_rectangle(445, 100, 445 + 167, 100 + 260, outline='black', width=5)
border_taverne2 = canvas.create_rectangle(655, 100, 655 + 167, 100 + 260, outline='black', width=5)

border_rafraichir_taverne = canvas.create_rectangle(960, 180, 1100, 240, outline='black', width=5)
border_vendre_serviteur = canvas.create_rectangle(1380, 420, 1380 + 167, 420 + 260, outline='black', width=5)
border_combat = canvas.create_rectangle(1350, 910, 1550, 990, outline='black', width=5)

border_board_liste = [border_joueur_waiting_0, border_joueur_waiting_1, border_joueur_waiting_2, border_joueur_waiting_3, border_joueur_waiting_4, border_joueur_waiting_5]
border_taverne_liste = [border_taverne0 , border_taverne1 , border_taverne2]


class Player:
    def __init__(self, nom):
        self.nom = nom
        self.hp = 20
        self.gold = 100
        self.taverne_tier = 3
        self.serviteurs_au_combat = [0,0,0,0]



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
        self.pv = 1
        self.atq = 1
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_1.png")

class Murloc_type_2(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Murloc acrobate"
        self.pv = 3
        self.atq = 1
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_2.png")

class Murloc_type_3(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Murloc ecuyer"
        self.pv = 4
        self.atq = 4
        self.tier = 2
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_3.png")

class Murloc_type_4(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Le sage vert"
        self.pv = 6
        self.atq = 6
        self.tier = 3
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_4.png")

class Paladin_type_1(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
        self.nom = "Guerrier sacré"
        self.pv = 3
        self.atq = 1
        self.tier = 1
        self.tribe = "Paladin"
        self.image = tk.PhotoImage(file="Images/Paladin_1.png")

class Bete_type_1(Serviteur):
    def __init__(self, id_serviteur):
        super().__init__(id_serviteur)
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

Liste_serviteurs = []       #Liste vide pour le moment, chaque fois que l'on crée un serviteur, on le rajoutera à cette liste.

colors_taverne = [0,0,0]
colors_board = [0,0,0,0,0,0]
colors_terrain = [0,0,0,0]

image_void = tk.PhotoImage(file="Images/void.png")

image_taverne = [image_void, image_void, image_void]    #Image taverne stock les objets de type image que l'on crée afin de pouvoir afficher les images.
emplacement_taverne_libre = [0,0,0]    # 0 correspond à une place libre, on met le nom du serviteur si la place est occupée
image_board = [image_void, image_void, image_void, image_void, image_void, image_void]
emplacement_board_libre = [0,0,0,0,0,0]
image_terrain = [image_void, image_void, image_void, image_void]
emplacement_terrain_libre = [0,0,0,0]

#Texte :
Message_bienvenue = tk.Label(fenetre, text="Bienvenue dans la taverne!", font=("Calibri", 18), fg="red", bg='#c0c0c0')
Message_bienvenue.place(x=700, y=35)

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

Message_vente1 = tk.Label(fenetre, text="Vendez ici vos serviteurs", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_vente2 = tk.Label(fenetre, text="pour recuperer 1 gold", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_vente_fleche = tk.Label(fenetre, text="--->", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_vente1.place(x = 1140, y = 480)
Message_vente2.place(x = 1150, y = 505)
Message_vente_fleche.place(x = 1220, y = 535)

Message_board1 = tk.Label(fenetre, text="Placez ici les serviteurs", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_board2 = tk.Label(fenetre, text="que vous achetez", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_board_fleche = tk.Label(fenetre, text="<---", font=("Calibri", 14), fg="black", bg='#c0c0c0')
Message_board1.place(x = 1270, y = 740)
Message_board2.place(x = 1290, y = 765)
Message_board_fleche.place(x = 1342, y = 793)

message_rafraichir = tk.Label(fenetre, text="Refresh tavern", font=("Calibri", 14), fg="black", bg='#c0c0c0')
message_rafraichir.place(x = 972, y = 250)
message_rafraichir_cout = tk.Label(fenetre, text="cost : 1 gold", font=("Calibri", 13), fg="black", bg='#c0c0c0')
message_rafraichir_cout.place(x = 980, y = 275)

message_combat = tk.Label(fenetre, text="COMBAT", font=("Calibri", 15), fg="black", bg='#c0c0c0')
message_combat.place(x = 1405, y = 870)

#Paramètres du joueur
Joueur = Player("M. Vilela Monteiro")
Adversaire = Player("Ennemy")
nom_joueur = tk.Label(fenetre, text=" " +Joueur.nom+ " ", font=("Calibri", 20), fg="red", bg='#c0c0c0', relief='solid',bd=2)
nom_joueur.place(x=1300, y=100)
gold_joueur_message = tk.Label(fenetre, text="Your gold :", font=("Calibri", 18), fg="black", bg='#c0c0c0')
gold_joueur_message.place(x=1300, y=190)
gold_joueur = tk.Label(fenetre, text=Joueur.gold, font=("Calibri", 18), fg="black", bg='#c0c0c0')
gold_joueur.place(x=1420, y=190)
tier_joueur_message = tk.Label(fenetre, text="Your tavern tier :", font=("Calibri", 18), fg="black", bg='#c0c0c0')
tier_joueur_message.place(x=1300, y=160)
tier_joueur = tk.Label(fenetre, text=Joueur.taverne_tier, font=("Calibri", 18), fg="black", bg='#c0c0c0')
tier_joueur.place(x=1480, y=160)

def on_mouse_click(event):
    # Récupérer les coordonnées absolues de la souris
    abs_x, abs_y = event.widget.winfo_pointerxy()
    # Récupérer les coordonnées de la fenêtre Tkinter (obligatoire pour déplacer la fenêtre
    fenetre_x, fenetre_y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
    # Calculer les coordonnées relatives à la fenêtre Tkinter
    rel_x, rel_y = abs_x - fenetre_x, abs_y - fenetre_y

    #Pour changer la couleur du rectangle autour des cartes de la taverne
    if 235 < rel_x < 235 + 167 and 100 < rel_y < 100 + 260 and emplacement_taverne_libre[0] != 0:
        clic_sur_taverne(0)
    if 445 < rel_x < 445 + 167 and 100 < rel_y < 100 + 260 and emplacement_taverne_libre[1] != 0:
        clic_sur_taverne(1)
    if 655 < rel_x < 655 + 167 and 100 < rel_y < 100 + 260 and emplacement_taverne_libre[2] != 0:
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
    if 25 < rel_x < 25 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[0] != 0:
        clic_sur_board_occupe(0)
    if 235 < rel_x < 235 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[1] != 0:
        clic_sur_board_occupe(1)
    if 445 < rel_x < 445 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[2] != 0:
        clic_sur_board_occupe(2)
    if 655 < rel_x < 655 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[3] != 0:
        clic_sur_board_occupe(3)
    if 865 < rel_x < 865 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[4] != 0:
        clic_sur_board_occupe(4)
    if 1075 < rel_x < 1075 + 167 and 720 < rel_y < 720 + 260 and emplacement_board_libre[5] != 0:
        clic_sur_board_occupe(5)
    #Pour le déplacement d'une carte de la main du joueur vers le terrain
    if 235 < rel_x < 235 + 167 and 420 < rel_y < 420 + 260 and emplacement_terrain_libre[0] == 0:
        poser_un_serviteur(235, 420, 0)
    if 445 < rel_x < 445 + 167 and 420 < rel_y < 420 + 260 and emplacement_terrain_libre[1] == 0:
        poser_un_serviteur(445, 420, 1)
    if 655 < rel_x < 655 + 167 and 420 < rel_y < 420 + 260 and emplacement_terrain_libre[2] == 0:
        poser_un_serviteur(655, 420, 2)
    if 865 < rel_x < 865 + 167 and 420 < rel_y < 420 + 260 and emplacement_terrain_libre[3] == 0:
        poser_un_serviteur(865, 420, 3)
    #Pour rafraichir la taverne :
    if 960 < rel_x < 1100 and 180 < rel_y < 240:
        refresh_taverne(Joueur)
    #Pour vendre un serviteur :
    if 1380 < rel_x < 1547 and 420 < rel_y < 680:
        vendre_serviteur()
    #Pour lancer le combat :
    if 1350 < rel_x < 1550 and 910 < rel_y < 990:
        préparation_combat(Joueur, Adversaire)
        #fenetre.mainloop()
        Lancer_combat(Joueur,Adversaire)

def clic_sur_taverne(colors_index):
    global colors_taverne
    if colors_taverne[colors_index] == 0:
        colors_taverne = [0,0,0]
        colors_taverne[colors_index] = 1
    else:
        colors_taverne[colors_index] = 0
    for i in range (3):
        if colors_taverne[i] == 0:
            canvas.itemconfigure(border_taverne_liste[i], outline='black')
        if colors_taverne[i] == 1:
            canvas.itemconfigure(border_taverne_liste[i], outline='red')

def clic_sur_board_vide(x,y, indice_board):
    global colors_taverne, emplacement_taverne_libre, colors_board, Joueur, image_board
    for indice_taverne in range(3):
        if colors_taverne[indice_taverne] == 1:
            if Joueur.gold >= 3:
                canvas.delete(image_board[indice_board])
                canvas.coords(image_taverne[indice_taverne], x, y)
                image_board[indice_board] = image_taverne[indice_taverne]
                image_taverne[indice_taverne] = canvas.create_image(235 + indice_taverne*210, 100, anchor=tk.NW, image=image_void)
                colors_taverne[indice_taverne] = 0
                canvas.itemconfigure(border_taverne_liste[indice_taverne], outline='black')
                emplacement_board_libre[indice_board] = emplacement_taverne_libre[indice_taverne]
                emplacement_taverne_libre[indice_taverne] = 0
                colors_board[indice_board] = 1 #Il est necessaire de changer la couleur de la bordure vu l'ordre des évènements
                Joueur.gold = Joueur.gold - 3
                mise_a_jour_systeme_taverne()
            else : print("You need to have 3 gold to buy a card")


def poser_un_serviteur(x,y, indice_terrain):
    global colors_board, emplacement_board_libre, colors_terrain
    for indice_board in range(6):
        if colors_board[indice_board] == 1:
            canvas.delete(image_terrain[indice_terrain])
            canvas.coords(image_board[indice_board], x, y)
            image_terrain[indice_terrain] = image_board[indice_board]
            image_board[indice_board] = canvas.create_image(25 + indice_board*210, 720, anchor=tk.NW, image=image_void)
            colors_board[indice_board] = 0
            canvas.itemconfigure(border_board_liste[indice_board], outline='black')
            emplacement_terrain_libre[indice_terrain] = emplacement_board_libre[indice_board]
            emplacement_board_libre[indice_board] = 0
            colors_terrain[indice_terrain] = 1
            mise_a_jour_systeme_taverne()


def clic_sur_board_occupe(colors_index):
    global colors_board
    if colors_board[colors_index] == 0:
        colors_board = [0,0,0,0,0,0]
        colors_board[colors_index] = 1
    else:
        colors_board[colors_index] = 0
    for i in range (6):
        if colors_board[i] == 0:
            canvas.itemconfigure(border_board_liste[i], outline='black')
        if colors_board[i] == 1:
            canvas.itemconfigure(border_board_liste[i], outline='red')

def clic_sur_terrain_occupe(colors_index):
    global colors_terrain, colors_board
    if colors_board[colors_index] == 0:
        colors_board = [0,0,0,0,0,0]
        colors_board[colors_index] = 1
    else:
        colors_board[colors_index] = 0
    for i in range (6):
        if colors_board[i] == 0:
            canvas.itemconfigure(border_board_liste[i], outline='black')
        if colors_board[i] == 1:
            canvas.itemconfigure(border_board_liste[i], outline='red')


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
        if nb_aléatoire == 4:
            Liste_serviteurs[id_serviteur] = Murloc_type_3(id_serviteur)
        if nb_aléatoire == 5:
            Liste_serviteurs[id_serviteur] = Murloc_type_4(id_serviteur)

        image_taverne[i] = canvas.create_image(235 + i*210, 100, anchor=tk.NW, image=Liste_serviteurs[id_serviteur].image)
        emplacement_taverne_libre[i] = Liste_serviteurs[id_serviteur]
        mise_a_jour_systeme_taverne()



def initialisation_board_et_terrain():
    for i in range (6):
        image_board[i] = canvas.create_image(25 + 210 * i, 720, anchor=tk.NW, image=image_void)
    for i in range(4):
        image_terrain[i] = canvas.create_image(235 + 210 * i, 420, anchor=tk.NW, image=image_void)



label_liste_taverne = [0,0,0,0,0,0] # Les 3 premiers carractères sont les points d'attaque des 3 serviteurs placés dans la taverne, les 3 suivants sont leur point de vie
label_liste_board = [0,0,0,0,0,0,0,0,0,0,0,0] #Idem que précédemment mais il y a 6 serviteurs donc 12 carractères
label_liste_terrain = [0,0,0,0,0,0,0,0]
def mise_a_jour_systeme_taverne():
    global label_liste_taverne,label_liste_board, gold_joueur
    #On détruit d'abord les pv/points d'attaque affichés précemment
    for i in range(6):
        if label_liste_taverne[i] != 0:
            label_liste_taverne[i].destroy()
            label_liste_taverne[i] = 0
    for i in range(12):
        if label_liste_board[i] != 0:
            label_liste_board[i].destroy()
            label_liste_board[i] = 0
    for i in range(8):
        if label_liste_terrain[i] != 0:
            label_liste_terrain[i].destroy()
            label_liste_terrain[i] = 0

    #On affiche les nouveaux points d'attaque et points de vie
    for i in range(3):
        if emplacement_taverne_libre[i] != 0:
            label_liste_taverne[i] = tk.Label(fenetre, text=emplacement_taverne_libre[i].atq, font=("Calibri", 12), fg="blue", bg="wheat")
            label_liste_taverne[i].place(x=260 + i * 210, y=266)
            label_liste_taverne[i+3] = tk.Label(fenetre, text=emplacement_taverne_libre[i].pv, font=("Calibri", 12), fg="red", bg="wheat")
            label_liste_taverne[i+3].place(x=365 +i*210, y=266)

    for i in range(6):
        if emplacement_board_libre[i] != 0:
            label_liste_board[i] = tk.Label(fenetre, text=emplacement_board_libre[i].atq, font=("Calibri", 12), fg="blue", bg="wheat")
            label_liste_board[i].place(x=50 + i * 210, y=886)
            label_liste_board[i+3] = tk.Label(fenetre, text=emplacement_board_libre[i].pv, font=("Calibri", 12), fg="red", bg="wheat")
            label_liste_board[i+3].place(x=155 + i * 210, y=886)

    for i in range(4):
        if emplacement_terrain_libre[i] != 0:
            label_liste_terrain[i] = tk.Label(fenetre, text=emplacement_terrain_libre[i].atq, font=("Calibri", 12), fg="blue", bg="wheat")
            label_liste_terrain[i].place(x=260 + i * 210, y=586)
            label_liste_terrain[i+3] = tk.Label(fenetre, text=emplacement_terrain_libre[i].pv, font=("Calibri", 12), fg="red", bg="wheat")
            label_liste_terrain[i+3].place(x=365 + i * 210, y=586)

    gold_joueur.destroy()
    gold_joueur = tk.Label(fenetre, text=Joueur.gold, font=("Calibri", 18), fg="black", bg='#c0c0c0')
    gold_joueur.place(x=1420, y=190)


def refresh_taverne(Joueur):
    if Joueur.gold >= 1:
        for i in range(3):
            canvas.delete(image_taverne[i])
        Joueur.gold = Joueur.gold - 1
        remplissage_taverne(Joueur.taverne_tier)


def vendre_serviteur():
    global Joueur, image_board, colors_board
    for i in range(6):
        if colors_board[i] == 1:
            colors_board[i] = 0
            image_board[i] = canvas.create_image(25 + i*210, 720, anchor=tk.NW, image=image_void)
            canvas.itemconfigure(border_board_liste[i], outline='black')
            emplacement_board_libre[i] = 0
            Joueur.gold += 1
    mise_a_jour_systeme_taverne()


#Création des 4 adversaires :
liste_opposants = [0,0,0,0]
for i in range(4):
    liste_opposants[i] = Murloc_type_4(i+1000)


def Bataille2(p1,p2, p1_next_battler, p2_next_battler):
    while (p1.serviteurs_au_combat[p1_next_battler] == 0):      # Boucle pour trouver un serviteur du joueur 1
        p1_next_battler += 1
        if (p1_next_battler == 4):
            p1_next_battler = 0

    target = rd.randint(0, 3)
    while (p2.serviteurs_au_combat[target] == 0):           # Boucle pour trouver une cible : un serviteur du joueur 2
        target = rd.randint(0, 3)

    a = p1.serviteurs_au_combat[p1_next_battler].attaquer(p2.serviteurs_au_combat[target])      # a permet de déterminer quels serviteurs sont morts
    if (a == 1 or a == 3):
        p1.serviteurs_au_combat[p1_next_battler] = 0
    if (a == 2 or a == 3):
        p2.serviteurs_au_combat[p1_next_battler] = 0
    p1_next_battler += 1
    time.sleep(1)

def Lancer_combat(p1,p2):
    next_attacker = rd.randint(1,2)     #Défini si c'est le joueur 1 qui commence à attaquer ou si c'est le 2ème. De plus, cette variable sera mise à jour à chaque attaque.
    p1_next_battler = 0
    p2_next_battler = 0
    while (p1.serviteurs_au_combat != [0,0,0,0] and p2.serviteurs_au_combat != [0,0,0,0]):
        print(p1.serviteurs_au_combat)
        print(p2.serviteurs_au_combat)
        if (next_attacker == 1):
            Bataille2(p1,p2, p1_next_battler, p2_next_battler)
            next_attacker = 2
        else :
            Bataille2(p2,p1, p2_next_battler, p1_next_battler)
            next_attacker = 1
    print("fin du combat")

def préparation_combat(p1,p2):
    global emplacement_terrain_libre, liste_opposants
    image_combat = [0, 0, 0, 0]
    label_combat_liste = [0,0,0,0,0,0,0,0]
    image_opposant = [0,0,0,0]
    label_opposant_liste = [0,0,0,0,0,0,0,0]
    canvas_combat = tk.Canvas(fenetre, width=1600, height=1000)
    canvas_combat.configure(bg='#c0c0c0')
    canvas.grid_remove()
    canvas_combat.grid()
    for i in range(4):
        if emplacement_terrain_libre[i] != 0:
            image_combat[i] = canvas_combat.create_image(235 + i * 210, 700, anchor=tk.NW, image=emplacement_terrain_libre[i].image)
            label_combat_liste[i] = tk.Label(fenetre, text=emplacement_terrain_libre[i].atq, font=("Calibri", 12), fg="blue", bg="wheat")
            label_combat_liste[i].place(x=260 + i * 210, y=866)
            label_combat_liste[i + 3] = tk.Label(fenetre, text=emplacement_terrain_libre[i].pv, font=("Calibri", 12), fg="red", bg="wheat")
            label_combat_liste[i + 3].place(x=365 + i * 210, y=866)
        if emplacement_terrain_libre[i] == 0:
            image_combat[i] = canvas_combat.create_image(235 + i * 210, 700, anchor=tk.NW, image=image_void)

        #Affichage des adversaires :
        image_opposant[i] = canvas_combat.create_image(235 + i * 210, 120, anchor=tk.NW, image=liste_opposants[i].image)
        label_opposant_liste[i] = tk.Label(fenetre, text=liste_opposants[i].atq, font=("Calibri", 12), fg="blue", bg="wheat")
        label_opposant_liste[i].place(x=260 + i * 210, y=286)
        label_opposant_liste[i + 3] = tk.Label(fenetre, text=liste_opposants[i].pv, font=("Calibri", 12), fg="red", bg="wheat")
        label_opposant_liste[i + 3].place(x=365 + i * 210, y=286)

    #Copie des unités
    p1.serviteurs_au_combat = emplacement_terrain_libre
    p2.serviteurs_au_combat = liste_opposants



#Programme




initialisation_board_et_terrain()
remplissage_taverne(1)






fenetre.bind("<Button-1>", on_mouse_click)
fenetre.mainloop()



