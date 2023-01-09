import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("1500x1000")  # Taille de la fenêtre


class Battler:
    def __init__(self, nom, pv, attaque, tier, image):
        self.nom = nom
        self.pv = pv
        self.atq = attaque
        self.tier = tier
        self.image = image

    def attaquer(self, opposant):
        opposant.pv = opposant.pv - self.atq
        self.pv = self.pv - opposant.atq
        a=0
        if (self.pv <= 0):
            a = a + 1             #La variable a permet de savoir si des combattants sont morts pendant l'attaque, si battler1 est mort a = 1, si battler 2 est mort a = 2 et si les deux sont morts a =3
        if (opposant.pv <= 0):
            a = a + 2
        return a


# Tribes :

class Murloc(Battler):
  def __init__(self, nom, pv, attaque, tier, image):
    super().__init__(nom, pv, attaque, tier, image)
    self.tribe = "Murloc"



# Cards :

class Murloc_type_1(Murloc):
  def __init__(self):
    super().__init__("Murloc_type_1", 3, 1, 1, tk.PhotoImage(file="Images/Murloc_1.png"))
    self.tribe = self.tribe


test = Murloc_type_1()
print(test.image)


