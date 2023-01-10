import tkinter as tk

def hitbox_clicked(event):
    print("Hitbox clicked!")

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Chargement de l'image
image = tk.PhotoImage(file="Images/Murloc_1.png")
canvas.create_image(0, 0, image=image, anchor="nw")

# Créer un frame transparent qui contient la hitbox
hitbox_frame = tk.Frame(root, bg='-transparentcolor',bd=0,width=100,height=50)
hitbox_frame.place(x=50, y=50)

hitbox_frame.bind("<Button-1>", hitbox_clicked)

root.mainloop()