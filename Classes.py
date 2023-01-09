
class Player:
    def __init__(self, nom):
        self.nom = nom
        self.gold = 3
        self.hp = 20
        self.battlers_on_field = ["void","void"]
        self.battlers_waiting = []





class Battler:
    def __init__(self, nom, pv, attaque, tier):
        self.nom = nom
        self.pv = pv
        self.atq = attaque
        self.tier = tier

    def attaquer(self, opposant):
        opposant.pv = opposant.pv - self.atq
        self.pv = self.pv - opposant.atq
        if (self.pv <= 0):
            print("your mob is dead")
        if (opposant.pv <= 0):
            print("opponant mob is dead")



# Tribes :

class Murloc(Battler):
  def __init__(self, nom, pv, attaque, tier):
    super().__init__(nom, pv, attaque, tier)
    self.tribe = "Murloc"



# Cards :

class Murloc_type_1(Murloc):
  def __init__(self):
    super().__init__("Murloc_type_1", 3, 1, 1)
    self.tribe = self.tribe

class Murloc_type_2(Murloc):
  def __init__(self):
    super().__init__("Murloc_type_1", 4, 2, 2)
    self.tribe = self.tribe




#self.state("zoomed")       --> Permet d'avoir une fenetre de la taille de l'écran
        self.geometry("1500x900+100+100")
        self.configure(bg="white")
        # Charge les images à partir des fichiers "image1.png" et "image2.png"
        self.image1 = tk.PhotoImage(file="Images/Murloc_2.png")
        #self.image2 = tk.PhotoImage(file="Images/Murloc_1.png")

        # Crée deux widgets Label pour afficher les images
        self.label1 = tk.Label(self, image=self.image1)
        #self.label2 = tk.Label(self, image=self.image2)

        # Place les widgets à des positions spécifiques dans la fenêtre
        self.label1.place(x=50, y=50)
        #self.label2.place(x=300, y=100, width=150, height=150)