import tkinter as tk
import random as rd
import time


# Variables globales

lieu = "taverne1" # Permet de savoir si l'on se trouve à la taverne ou au combat
indice_taverne = 1  # Permet de savoir si on se trouve dans la taverne du joueur 1 ou 2
Nombre_combats = 0 # Augmente de 1 après chaque phase de combat, permet de connaître le tour du jeu



fenetre = tk.Tk()
fenetre.geometry("1600x1000")  # Taille de la fenêtre
fenetre.configure(bg='#c0c0c0')

# Configuration des canvas

canvas_taverne1 = tk.Canvas(fenetre, width=1600, height=1000)    #Canvas utilisé pour l'interface taverne
canvas_taverne1.configure(bg='#c0c0c0')      # Couleur gris clair
canvas_taverne1.grid()  #Affiche ce canva à l'écran

canvas_taverne2 = tk.Canvas(fenetre, width=1600, height=1000)
canvas_taverne2.configure(bg='#c0c0c0')

canvas_combat = tk.Canvas(fenetre, width=1600, height=1000)     #Canvas utilisé pour l'interface combat
canvas_combat.configure(bg='#c0c0c0')

canvas_texte = tk.Canvas(fenetre, width=1600, height=1000)     #Canvas utilisé pour l'interface textuelle
canvas_texte.configure(bg='#c0c0c0')

# On importe l'image vide, utile quand il n'y a pas de serviteur sur une tuile
image_void = tk.PhotoImage(file="Images/void.png")


class Player:
    def __init__(self, nom, canvas_taverne):
        self.nom = nom
        self.hp = 20
        self.hp_max = 20
        self.gold = 3       # Le joueur commence avec 4 gold car on remplis automatiquement sa taverne avant qu'il ne commence à jouer ce qui coute 1 gold, il n'a donc que 3 gold au démarrage
        self.taverne_tier = 1
        self.prix_upgrade_taverne = 5
        self.next_battler = 0
        # Pour le combat :
        self.canvas_taverne = canvas_taverne
        self.Tiles_combat = []

        # Création des 3 listes dans les quelles nous allons placer nos objets de type Tiles
        self.Tiles_taverne = []  # Liste de 3
        self.Tiles_main = []  # Liste de 6
        self.Tiles_plateau = []  # Liste de 4
        # Remplissage des 3 listes
        for i in range(3):
            self.Tiles_taverne = self.Tiles_taverne + [Tile("Taverne" + str(i), self.canvas_taverne, 235 + 210 * i, 100)]
        for i in range(6):
            self.Tiles_main = self.Tiles_main + [Tile("Main" + str(i), self.canvas_taverne, 25 + 210 * i, 720)]
        for i in range(4):
            self.Tiles_plateau = self.Tiles_plateau + [Tile("Plateau" + str(i), self.canvas_taverne, 235 + 210 * i, 420)]

        # Création d'une liste regroupant les 3 listes précédentes pour que cela soit + pratique
        self.Tiles_total_taverne = self.Tiles_taverne + self.Tiles_main + self.Tiles_plateau  # Liste de 13

        # Necessaire pour de l'affichage supplémentaire
        self.affichage_tier = 0
        self.affichage_gold = 0
        self.affichage_cout_upgrade_taverne = 0

    def initialisation_combat(self, position, Tiles):
        self.next_battler = 0
        if position == 1:
            y = 720    # La variable y permet de placer un joueur en haut de l'écran et l'autre en bas
        if position == 2:
            y = 120
        self.Tiles_combat = [0,0,0,0]
        for i in range(4):
            self.Tiles_combat[i] = Tile.constructeur_copie(235 + 210 * i, y, Tiles[i])
            self.Tiles_combat[i].update()

    def degat_subis(self, opposant):
        count = 0
        for i in range(4):
            if opposant.Tiles_combat[i].serviteur != 0:
                self.hp = self.hp - opposant.Tiles_combat[i].serviteur.tier
                count += opposant.Tiles_combat[i].serviteur.tier
        print(self.nom + " a subis " + str(count) + " degats")

    def mise_a_jour_fin_combat(self):
        global Nombre_combats
        self.gold += 1  # Sert à payer les frais de taverne quand on rafraichit
        rafraichir_taverne(self)
        self.gold = 3 + Nombre_combats
        if self.gold > 10:
            self.gold = 10
        self.prix_upgrade_taverne -= 1
        if self.prix_upgrade_taverne < 0:
            self.prix_upgrade_taverne = 0
        affichage_texte_taverne_dynamique(self)

    def mort(self, opposant):
        global lieu
        lieu = "FIN"
        canvas_combat.grid_remove()
        canvas_texte.grid()
        texte_fin = tk.Label(canvas_texte, text=self.nom + " a été vaincu, victoire de " + opposant.nom, font=("Times New Roman", 40), fg="blue", bg='#c0c0c0')
        texte_fin.place(x=350, y=400)
        texte_pv_fin1 = tk.Label(canvas_texte, text="Points de vie de " + self.nom + " : " + str(self.hp), font=("Arial", 25), fg="black", bg='#c0c0c0')
        texte_pv_fin1.place(x=425, y=500)
        texte_pv_fin2 = tk.Label(canvas_texte, text="Points de vie de " + opposant.nom + " : " + str(opposant.hp),font=("Arial", 25), fg="black", bg='#c0c0c0')
        texte_pv_fin2.place(x=425, y=540)


class Serviteur:
    def __init__(self):
        self.nom = ""
        self.hp = 0
        self.atq = 0
        self.tier = 0
        self.tribe = ""
        self.image = None
        self.cris_de_guerre = 0

    def attaquer(self, opposant):
        opposant.hp = opposant.hp - self.atq
        self.hp = self.hp - opposant.atq
        a = 0
        if (self.hp <= 0):
            a = a + 1  # La variable a permet de savoir si des combattants sont morts pendant l'attaque, si battler1 est mort a = 1, si battler 2 est mort a = 2 et si les deux sont morts a =3
        if (opposant.hp <= 0):
            a = a + 2
        return a

#Serviteurs

class Murloc_type_1(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Murloc explorateur"
        self.hp = 1
        self.atq = 1
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_1.png")
        self.cris_de_guerre = None
        self.apparition = None

class Murloc_type_2(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Murloc acrobate"
        self.hp = 3
        self.atq = 1
        self.tier = 1
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_2.png")
        self.cris_de_guerre = [0,0]
        self.apparition = None

class Murloc_type_3(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Murloc ecuyer"
        self.hp = 4
        self.atq = 4
        self.tier = 2
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_3.png")
        self.cris_de_guerre = None
        self.apparition = [0,[1,1]]

class Murloc_type_4(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Le sage vert"
        self.hp = 6
        self.atq = 6
        self.tier = 3
        self.tribe = "Murloc"
        self.image = tk.PhotoImage(file="Images/Murloc_4.png")
        self.cris_de_guerre = None
        self.apparition = None

class Paladin_type_1(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Guerrier sacré"
        self.hp = 3
        self.atq = 1
        self.tier = 1
        self.tribe = "Paladin"
        self.image = tk.PhotoImage(file="Images/Paladin_1.png")
        self.cris_de_guerre = None
        self.apparition = None

class Bete_type_1(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "La bete sanguinaire"
        self.hp = 4
        self.atq = 2
        self.tier = 1
        self.tribe = "Bete"
        self.image = tk.PhotoImage(file="Images/Bete_1.png")
        self.cris_de_guerre = None
        self.apparition = None

class Bete_type_2(Serviteur):
    def __init__(self):
        super().__init__()
        self.nom = "Bulbon the beast"
        self.hp = 5
        self.atq = 5
        self.tier = 4
        self.tribe = "Bete"
        self.image = tk.PhotoImage(file="Images/Bete_2.png")
        self.cris_de_guerre = None
        self.apparition = [1,[2,2]]


# Dictionnaire de tous les serviteurs existants
Liste_cartes_tier1 = [Murloc_type_1, Murloc_type_2, Paladin_type_1, Bete_type_1]
Liste_cartes_tier2 = Liste_cartes_tier1 + [Murloc_type_3]
Liste_cartes_tier3 = Liste_cartes_tier2 + [Murloc_type_4]
Liste_cartes_tier4 = Liste_cartes_tier3 + [Bete_type_2]

Liste_tier = [Liste_cartes_tier1 , Liste_cartes_tier2, Liste_cartes_tier3, Liste_cartes_tier4]



class Tile:
    def __init__(self, nom, canvas, x, y):
        self.nom = nom
        self.x = x  # Coordonnées du coin en haut à gauche de l'emplacement
        self.y = y
        self.largeur = 167
        self.longueur = 260
        self.image = image_void
        self.color = "black"
        self.canvas = canvas    # Permet de savoir sur quel canvas se situe l'objet
        self.serviteur = 0  #Permet de savoir quel serviteur est sur la tuile, vaut 0 si il n'y a pas de serviteur
        self.border = self.canvas.create_rectangle(x, y, x + self.largeur, y + self.longueur, outline=self.color, width=5)
        self.image_affichage = self.canvas.create_image(x, y, anchor=tk.NW, image=self.image)
        self.atq_affichage = 0
        self.hp_affichage = 0

    @classmethod
    def constructeur_copie(cls, x, y, Tiles):
        nom = "Tile_copie"
        objet = cls(nom, canvas_combat, x , y)

        if Tiles.serviteur != 0:
            objet.serviteur = Serviteur()
            objet.serviteur.nom = Tiles.serviteur.nom
            objet.serviteur.hp = Tiles.serviteur.hp
            objet.serviteur.atq = Tiles.serviteur.atq
            objet.serviteur.tier = Tiles.serviteur.tier
            objet.serviteur.tribe = Tiles.serviteur.tribe
            objet.serviteur.image = Tiles.serviteur.image
            objet.serviteur.cris_de_guerre = Tiles.serviteur.cris_de_guerre

        return objet

    def update_bordure(self):
        self.canvas.delete(self.border)
        self.border = self.canvas.create_rectangle(self.x, self.y, self.x + self.largeur, self.y + self.longueur, outline=self.color, width=5)

    def update_image(self):
        # On supprime l'image affichée précédemment
        self.canvas.delete(self.image_affichage)
        #Si un serviteur est posé sur cette tuile, l'image de la tuile est l'image du serviteur
        if self.serviteur != 0:
            self.image = self.serviteur.image
        #Sinon l'image est l'image du vide
        else :
            self.image = image_void
        self.image_affichage = self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.image)

    def update_stats(self):
        if self.atq_affichage != 0:
            self.atq_affichage.destroy()
        if self.serviteur != 0:
            self.atq_affichage = tk.Label(self.canvas, text=self.serviteur.atq, font=("Calibri", 12), fg="blue", bg="wheat")
            self.atq_affichage.place(x=self.x + 25, y=self.y + 166)
        if self.hp_affichage != 0:
            self.hp_affichage.destroy()
        if self.serviteur != 0:
            self.hp_affichage = tk.Label(self.canvas, text=self.serviteur.hp, font=("Calibri", 12), fg="red", bg="wheat")
            self.hp_affichage.place(x=self.x + 130, y=self.y + 166)

    def update(self):
        self.update_bordure()
        self.update_image()
        self.update_stats()

def affichage_texte_taverne_statique(Joueur):
    Message_bienvenue = tk.Label(Joueur.canvas_taverne, text="Bienvenue dans la taverne!", font=("Calibri", 18),fg="red",bg='#c0c0c0')
    Message_bienvenue.place(x=700, y=35)
    Message_taverne = tk.Label(Joueur.canvas_taverne, text="Achetez ici vos serviteurs", font=("Calibri", 14),fg="black",bg='#c0c0c0')
    Message_taverne.place(x=20, y=150)
    Message_taverne_fleche = tk.Label(Joueur.canvas_taverne, text="--->", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    Message_taverne_fleche.place(x=100, y=180)
    Message_terrain1 = tk.Label(Joueur.canvas_taverne, text="Placez ici vos serviteurs", font=("Calibri", 14),fg="black",bg='#c0c0c0')
    Message_terrain2 = tk.Label(Joueur.canvas_taverne, text="pour le combat", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    Message_terrain_fleche = tk.Label(Joueur.canvas_taverne, text="--->", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    Message_terrain1.place(x=20, y=480)
    Message_terrain2.place(x=50, y=505)
    Message_terrain_fleche.place(x=100, y=535)
    Message_vente1 = tk.Label(Joueur.canvas_taverne, text="Vendez ici vos serviteurs", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    Message_vente2 = tk.Label(Joueur.canvas_taverne, text="pour recuperer 1 gold", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    Message_vente_fleche = tk.Label(Joueur.canvas_taverne, text="--->", font=("Calibri", 14), fg="black", bg='#c0c0c0')
    Message_vente1.place(x=1140, y=480)
    Message_vente2.place(x=1150, y=505)
    Message_vente_fleche.place(x=1220, y=535)
    Message_board1 = tk.Label(Joueur.canvas_taverne, text="Placez ici les serviteurs", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    Message_board2 = tk.Label(Joueur.canvas_taverne, text="que vous achetez", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    Message_board_fleche = tk.Label(Joueur.canvas_taverne, text="<---", font=("Calibri", 14), fg="black", bg='#c0c0c0')
    Message_board1.place(x=1270, y=740)
    Message_board2.place(x=1290, y=765)
    Message_board_fleche.place(x=1342, y=793)
    message_rafraichir = tk.Label(Joueur.canvas_taverne, text="Refresh tavern", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    message_rafraichir.place(x=1070, y=272)
    message_rafraichir_cout = tk.Label(Joueur.canvas_taverne, text="cost : 1 gold", font=("Calibri", 13), fg="black",bg='#c0c0c0')
    message_rafraichir_cout.place(x=1085, y=297)
    message_up_taverne = tk.Label(Joueur.canvas_taverne, text="Upgrade tavern", font=("Calibri", 14), fg="black",bg='#c0c0c0')
    message_up_taverne.place(x=1070, y=142)
    if Joueur == J2:
        message_combat = tk.Label(Joueur.canvas_taverne, text="COMBAT", font=("Calibri", 15), fg="black", bg='#c0c0c0')
        message_combat.place(x=1405, y=870)
    if Joueur == J1:
        message_combat = tk.Label(Joueur.canvas_taverne, text="Fin du tour", font=("Calibri", 15), fg="black", bg='#c0c0c0')
        message_combat.place(x=1395, y=870)
    nom_joueur = tk.Label(Joueur.canvas_taverne, text=" " + Joueur.nom + " ", font=("Calibri", 20), fg="red",bg='#c0c0c0', relief='solid', bd=2)
    nom_joueur.place(x=1300, y=100)

    # Créations de rectangles servant de boutons pour le menu taverne :
    rectangle_ameliorer_taverne = Joueur.canvas_taverne.create_rectangle(910, 140, 1050, 200, outline='black', width=5)
    rectangle_rafraichir_taverne = Joueur.canvas_taverne.create_rectangle(910, 270, 1050, 330, outline='black', width=5)
    rectangle_vendre_serviteur = Joueur.canvas_taverne.create_rectangle(1380, 420, 1380 + 167, 420 + 260, outline='black', width=5)
    rectangle_combat = Joueur.canvas_taverne.create_rectangle(1350, 910, 1550, 990, outline='black', width=5)

def affichage_texte_taverne_dynamique(Joueur):
    if Joueur.affichage_tier != 0:
        Joueur.affichage_tier.destroy()
        Joueur.affichage_gold.destroy()
        Joueur.affichage_cout_upgrade_taverne.destroy()
    Joueur.affichage_tier = tk.Label(Joueur.canvas_taverne, text="Your tavern tier  :  "+str(Joueur.taverne_tier), font=("Calibri", 18), fg="black", bg='#c0c0c0')
    Joueur.affichage_tier.place(x=1300, y=190)
    Joueur.affichage_gold = tk.Label(Joueur.canvas_taverne, text="Your gold  :  "+str(Joueur.gold), font=("Calibri", 18), fg="black", bg='#c0c0c0')
    Joueur.affichage_gold.place(x=1300, y=220)
    Joueur.affichage_tier = tk.Label(Joueur.canvas_taverne, text=str(Joueur.hp) + " / " + str(Joueur.hp_max) +  " hp", font=("Calibri", 18), fg="black", bg='#c0c0c0')
    Joueur.affichage_tier.place(x=1300, y=145)
    Joueur.affichage_cout_upgrade_taverne = tk.Label(Joueur.canvas_taverne, text="cost : "+ str(Joueur.prix_upgrade_taverne)+" gold", font=("Calibri", 13), fg="black", bg='#c0c0c0')
    Joueur.affichage_cout_upgrade_taverne.place(x=1085, y=167)


def affichage_combat():
    global texte_lancer_combat
    recantangle_lancer_combat = canvas_combat.create_rectangle(1380, 480, 1500, 550, outline='black', width=5)
    texte_lancer_combat = tk.Label(canvas_combat, text="Cliquez ici pour lancer le combat", font=("Calibri", 14),fg="black",bg='#c0c0c0')
    texte_lancer_combat.place(x=1300, y=450)

def on_mouse_click(event,J1, J2):
    global lieu
    if lieu == "taverne1":
        player = J1
    if lieu == "taverne2":
        player = J2
    debug = 0
    # Récupérer les coordonnées absolues de la souris
    abs_x, abs_y = event.widget.winfo_pointerxy()
    # Récupérer les coordonnées de la fenêtre Tkinter (obligatoire pour déplacer la fenêtre
    fenetre_x, fenetre_y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
    # Calculer les coordonnées relatives à la fenêtre Tkinter
    rel_x, rel_y = abs_x - fenetre_x, abs_y - fenetre_y

    if lieu == "taverne1" or lieu == "taverne2":

        for i in range(4):
            if player.Tiles_plateau[i].x < rel_x < player.Tiles_plateau[i].x + player.Tiles_plateau[i].largeur and player.Tiles_plateau[i].y < rel_y < player.Tiles_plateau[i].y + player.Tiles_plateau[i].longueur and player.Tiles_plateau[i].image != image_void:
                echange_cartes_plateau(player, i)
        for i in range(13):
            if player.Tiles_total_taverne[i].x < rel_x < player.Tiles_total_taverne[i].x + player.Tiles_total_taverne[i].largeur and player.Tiles_total_taverne[i].y < rel_y < player.Tiles_total_taverne[i].y + player.Tiles_total_taverne[i].longueur and player.Tiles_total_taverne[i].image != image_void:
                clic_sur_carte(player, i)
        for i in range(6):
            if player.Tiles_main[i].x < rel_x < player.Tiles_main[i].x + player.Tiles_main[i].largeur and player.Tiles_main[i].y < rel_y < player.Tiles_main[i].y + player.Tiles_main[i].longueur and player.Tiles_main[i].image == image_void:
                clic_sur_main_vide(player, i)
        for i in range(4):
            if player.Tiles_plateau[i].x < rel_x < player.Tiles_plateau[i].x + player.Tiles_plateau[i].largeur and player.Tiles_plateau[i].y < rel_y < player.Tiles_plateau[i].y + player.Tiles_plateau[i].longueur and player.Tiles_plateau[i].image == image_void:
                clic_sur_plateau_vide(player, i)
        if 910 < rel_x < 1050 and 270 < rel_y < 330:
            rafraichir_taverne(player)
        if 910 < rel_x < 1050 and 140 < rel_y < 200:
            ameliorer_taverne(player)
        if 1380 < rel_x < 1547 and 420 < rel_y < 680:
            vendre_serviteur(player)
        if 1350 < rel_x < 1550 and 910 < rel_y < 960 and lieu == "taverne2":
            preparation_combat(J1,J2)
        if 1350 < rel_x < 1550 and 910 < rel_y < 960 and lieu == "taverne1":
            switch_to_tavern(J1, J2, 2)

    if lieu == "fin_combat":
        if 1380 < rel_x < 1500 and 480 < rel_y < 550:
            retour_taverne(J1,J2)
    if lieu == "combat":
        if 1380 < rel_x < 1500 and 480 < rel_y < 550 and debug == 0:    # Tentative de mettre une entité debug qui empecherait le spam du bouton (mais ca ne marche pas) :/
            debug = 1
            canvas_combat.update()
            lancer_combat(J1,J2)


def remplissage_taverne(player,tier):
    nb_cartes = len(Liste_tier[tier-1])
    for i in range(3):
        nb_aleatoire = rd.randint(0, nb_cartes-1)

        player.Tiles_taverne[i].serviteur = Liste_tier[tier-1][nb_aleatoire]()
        player.Tiles_taverne[i].update()

def rafraichir_taverne(player):
    if player.gold >= 1:
        for i in range(3):
            player.Tiles_taverne[i].serviteur = 0
        player.gold -= 1
        affichage_texte_taverne_dynamique(player)
        remplissage_taverne(player, player.taverne_tier)
    else :
        print("You need 1 gold to refresh tavern")

def vendre_serviteur(player):
    for i in range(3,13):
        if player.Tiles_total_taverne[i].color == "red":
            player.Tiles_total_taverne[i].color = "black"
            player.Tiles_total_taverne[i].serviteur = 0
            player.Tiles_total_taverne[i].update()
            player.gold += 1
            if player.gold > 10:
                player.gold = 10
            affichage_texte_taverne_dynamique(player)

def ameliorer_taverne(player):
    if player.taverne_tier != 4:
        if player.gold >= player.prix_upgrade_taverne:
            player.taverne_tier += 1
            player.gold -= player.prix_upgrade_taverne
            player.prix_upgrade_taverne = 5
            affichage_texte_taverne_dynamique(player)
        else :
            print("You need", player.prix_upgrade_taverne, "gold to upgrade tavern")
    if player.taverne_tier == 4:
        print("You are already max tier")

def clic_sur_carte(player, indice):
    a = "black"
    if player.Tiles_total_taverne[indice].color == "black":
        a = "red"
    for i in range(13):
        player.Tiles_total_taverne[i].color = "black"
        player.Tiles_total_taverne[i].update()
    player.Tiles_total_taverne[indice].color = a
    player.Tiles_total_taverne[indice].update()

def clic_sur_main_vide(player, indice):
    for i in range(3):
        if player.Tiles_taverne[i].color == "red":
            if player.gold >= 3:
                player.Tiles_taverne[i].color = "black"
                player.Tiles_main[indice].serviteur = player.Tiles_taverne[i].serviteur
                player.Tiles_taverne[i].serviteur = 0
                player.Tiles_main[indice].update()
                player.Tiles_taverne[i].update()
                player.gold -= 3
                affichage_texte_taverne_dynamique(player)


            else : print("You need to have 3 gold to buy a card")

def clic_sur_plateau_vide(player, indice):
    for i in range(6):
        if player.Tiles_main[i].color == "red":
            player.Tiles_main[i].color = "black"
            player.Tiles_plateau[indice].serviteur = player.Tiles_main[i].serviteur
            player.Tiles_main[i].serviteur = 0
            player.Tiles_plateau[indice].update()
            player.Tiles_main[i].update()
            if player.Tiles_plateau[indice].serviteur.cris_de_guerre != None:
                Cris_de_guerre(player, player.Tiles_plateau[indice].serviteur.cris_de_guerre[0],player.Tiles_plateau[indice].serviteur.cris_de_guerre[1])
            check_if_apparition(player, player.Tiles_plateau[indice].serviteur, indice)


def check_if_apparition(player, nouveau_serviteur, indice):
    for i in range(4):
        if player.Tiles_plateau[i].serviteur != 0:
            if player.Tiles_plateau[i].serviteur.apparition != None and i != indice:
                Apparition(player, nouveau_serviteur.tribe, i)


def echange_cartes_plateau(player, indice):
    for i in range(4):
        if i != indice:
            if player.Tiles_plateau[i].color == "red":
                player.Tiles_plateau[i].color = "black"
                player.Tiles_plateau[indice].color = "red" # Necessaire a cause de l'enchainement de conditions dans la fonction "on_mouse_click", sinon la bordure était de couleur noire
                temporaire = player.Tiles_plateau[indice].serviteur
                player.Tiles_plateau[indice].serviteur = player.Tiles_plateau[i].serviteur
                player.Tiles_plateau[i].serviteur = temporaire
                player.Tiles_plateau[indice].update()
                player.Tiles_plateau[i].update()

def preparation_combat(p1,p2):
    global lieu
    lieu = "combat"
    p2.canvas_taverne.grid_remove()
    canvas_combat.grid()
    affichage_combat()
    p1.initialisation_combat(1, p1.Tiles_plateau)
    p2.initialisation_combat(2, p2.Tiles_plateau)

def Bataille(p1,p2, next_attacker):
    while (p1.Tiles_combat[p1.next_battler].serviteur == 0):  # Boucle pour trouver un serviteur du joueur 1
        p1.next_battler += 1
        if (p1.next_battler == 4):
            p1.next_battler = 0

    target = rd.randint(0, 3)
    while (p2.Tiles_combat[target].serviteur == 0):  # Boucle pour trouver une cible : un serviteur du joueur 2
        target = rd.randint(0, 3)

    a = p1.Tiles_combat[p1.next_battler].serviteur.attaquer(p2.Tiles_combat[target].serviteur)
    if next_attacker == 1:
        p1.Tiles_combat[p1.next_battler].y -= 100
    if next_attacker == 2:
        p1.Tiles_combat[p1.next_battler].y += 100
    p1.Tiles_combat[p1.next_battler].update()
    p2.Tiles_combat[target].update()
    canvas_combat.update()
    time.sleep(1)
    if next_attacker == 1:
        p1.Tiles_combat[p1.next_battler].y += 100
    if next_attacker == 2:
        p1.Tiles_combat[p1.next_battler].y -= 100
    p1.Tiles_combat[p1.next_battler].update()
    if (a == 1 or a == 3):
        p1.Tiles_combat[p1.next_battler].serviteur = 0
        p1.Tiles_combat[p1.next_battler].update()
    if (a == 2 or a == 3):
        p2.Tiles_combat[target].serviteur = 0
        p2.Tiles_combat[target].update()
    p1.next_battler += 1
    if (p1.next_battler == 4):
        p1.next_battler = 0
    canvas_combat.update()
    time.sleep(1)

def lancer_combat(p1,p2):
    global lieu, texte_lancer_combat
    next_attacker = rd.randint(1,2)     #Défini si c'est le joueur 1 qui commence à attaquer ou si c'est le 2ème. De plus, cette variable sera mise à jour à chaque attaque.
    while (p1.Tiles_combat[0].serviteur != 0 or p1.Tiles_combat[1].serviteur != 0 or p1.Tiles_combat[2].serviteur != 0 or p1.Tiles_combat[3].serviteur != 0) and (p2.Tiles_combat[0].serviteur != 0 or p2.Tiles_combat[1].serviteur != 0 or p2.Tiles_combat[2].serviteur != 0 or p2.Tiles_combat[3].serviteur != 0):
        if (next_attacker == 1):
            Bataille(p1,p2, next_attacker)
            next_attacker = 2
        else :
            Bataille(p2, p1, next_attacker)
            next_attacker = 1
    lieu = "fin_combat"
    p1.degat_subis(p2)
    p2.degat_subis(p1)

    # Affichage de texte :
    texte_lancer_combat.destroy()
    texte_lancer_combat = tk.Label(canvas_combat, text="Cliquez ici pour rentrer à la taverne", font=("Calibri", 14), fg="black", bg='#c0c0c0')
    texte_lancer_combat.place(x=1295, y=450)

    # Cas où un joueur meurs
    if p1.hp <= 0:
        p1.mort(p2)
    if p2.hp <= 0:
        p2.mort(p1)


def retour_taverne(p1,p2):
    global lieu, Nombre_combats, texte_lancer_combat
    Nombre_combats += 1
    lieu = "taverne1"
    canvas_combat.grid_remove()
    p1.canvas_taverne.grid()
    p1.mise_a_jour_fin_combat()
    p2.mise_a_jour_fin_combat()
    #On supprime les éléments du canvas de combat :
    for i in range(4):
        p1.Tiles_combat[i].serviteur = 0
        p2.Tiles_combat[i].serviteur = 0
        p1.Tiles_combat[i].update()
        p2.Tiles_combat[i].update()
    texte_lancer_combat.destroy()
    canvas_combat.delete("all")


def switch_to_tavern(p1, p2, indice):
    global lieu, Nombre_combats
    lieu = "taverne"+str(indice)
    p1.canvas_taverne.grid_remove()
    p2.canvas_taverne.grid()
    affichage_texte_taverne_dynamique(p2)
    # On remplis la taverne si c'est le 1er tour de jeu :
    if Nombre_combats == 0:
        remplissage_taverne(p2, p2.taverne_tier)

#Bonus
def Cris_de_guerre(player, id_cris_de_guerre, option):
    if id_cris_de_guerre == 0:
        succes = 0
        for i in range(4):
            if player.Tiles_plateau[i].serviteur == 0 and succes == 0:
                player.Tiles_plateau[i].serviteur = Liste_cartes_tier4[option]()
                player.Tiles_plateau[i].update()
                succes = 1
                check_if_apparition(player, player.Tiles_plateau[i].serviteur, i)
                return(0)
        print("le plateau est plein")

def Apparition(player, tribe, indice):
    id_apparition = player.Tiles_plateau[indice].serviteur.apparition[0]
    option = player.Tiles_plateau[indice].serviteur.apparition[1]
    if id_apparition == 0:
        # id = 0 correspond à "donne un bonus d'attaque et ou de vie à un serviteur d'une certaine tribue"
        if tribe == "Murloc":
            target = rd.randint(0,3)
            while player.Tiles_plateau[target].serviteur == 0:
                target = rd.randint(0, 3)
            while player.Tiles_plateau[target].serviteur.tribe != "Murloc":
                target = rd.randint(0,3)
                while player.Tiles_plateau[target].serviteur == 0:
                    target = rd.randint(0, 3)
            player.Tiles_plateau[target].serviteur.atq += option[0]
            player.Tiles_plateau[target].serviteur.hp += option[1]
            player.Tiles_plateau[target].update()
    if id_apparition == 1:
        #id = 1 correspond à "gagne un bonus d'attaque et ou de vie si le serviteur invoqué est de la bonne tribue
        if tribe == "Bete":
            player.Tiles_plateau[indice].serviteur.atq += option[0]
            player.Tiles_plateau[indice].serviteur.hp += option[1]
            player.Tiles_plateau[indice].update()




nom = input("Entrez votre nom (Max 15 caractères) : ")
while not 0 < len(nom) <= 15:
    if len(nom) == 0:
        print("Veuillez mettre un caractère au minimum")
    if len(nom) > 15:
        print("15 caractères maximum!")
    nom = input("Entrez votre nom (Max 15 caractères) : ")
fenetre.lift()

# Paramètres du joueur
J1 = Player(nom, canvas_taverne1)
J2 = Player("Ennemy", canvas_taverne2)


remplissage_taverne(J1,J1.taverne_tier)
affichage_texte_taverne_statique(J1)
affichage_texte_taverne_statique(J2)
affichage_texte_taverne_dynamique(J1)


fenetre.bind("<Button-1>", lambda event: on_mouse_click(event, J1, J2))

fenetre.mainloop()
