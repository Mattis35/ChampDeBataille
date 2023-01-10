import tkinter as tk

def on_ok_button_click():
    name = entry.get()
    print(name)

fenetre = tk.Tk()

label = tk.Label(fenetre, text="Quel est votre nom?")
label.pack()

entry = tk.Entry(fenetre)
entry.pack()

ok_button = tk.Button(fenetre, text="OK", command=on_ok_button_click)
ok_button.pack()

fenetre.mainloop()
