import tkinter as tk

class Morpion:
    fenetre = tk.Tk() 
    fenetre.geometry("400x400")
    fenetre.title("Morpion Benjamin, Bilal, Souleimen")
    fenetre['bg'] = 'blue'
    fenetre.resizable(height=False, width=False)

    buttons = tkinter.Button(fenetre,)
    ecriture = tk.Label(fenetre,text="Morpy" bg="blue", fg="white" font=("Arial",20))

    fenetre.mainloop()

