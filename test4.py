import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("1600x1000")  # Taille de la fenêtre
fenetre.configure(bg='#c0c0c0')

canvas = tk.Canvas(fenetre, width=1600, height=1000)
canvas.grid()
canvas.configure(bg='#c0c0c0')  # Couleur gris clair

canvas_combat = tk.Canvas(fenetre, width=1600, height=1000)
canvas_combat.configure(bg='#c0c0c0')
canvas_combat.grid_remove()

image = tk.PhotoImage(file="Images/Murloc_1.png")

combat = canvas_combat.create_image(235, 720, anchor=tk.NW, image=image)



canvas.grid_remove()
canvas_combat.grid()


def show_main():
    canvas_combat.grid_remove()
    canvas.grid()



fenetre.mainloop()