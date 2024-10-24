import tkinter as tk
from tkinter import *
root = Tk()
harceleur = Canvas(root)

def lignes():
    root.geometry("500x400")
    root.title("Jeu de Morpion")
    harceleur.create_line(100, 0, 100, 500, width=2)#lignes verticales
    harceleur.create_line(0, 100, 300, 100, width=2)  #lignes hori 
    harceleur.create_line(200, 0, 200, 300, width=2) #ligne verti
    harceleur.create_line(0, 200, 300, 200, width=2) #lignes hori

def codejeu():
    

harceleur.pack()
lignes()
root.mainloop()
