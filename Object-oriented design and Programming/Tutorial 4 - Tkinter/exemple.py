from tkinter import *
from random import randint

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)

        # paramètres de la fenêtre
        self.title('Tirage aléatoire')
        self.geometry('300x100+400+400')

        # constitution de l'arbre de scène
        boutonLancer = Button(self, text='Tirage')
        boutonLancer.pack(side=BOTTOM, padx=5, pady=5)
        self.__texteResultat = StringVar()
        labelResultat = Label(self, textvariable=self.__texteResultat,bg='blue')
        labelResultat.pack(side=LEFT, padx=5, pady=5)
        boutonQuitter = Button(self, text='Quitter',bg="red")
        boutonQuitter.pack(side=RIGHT, padx=5, pady=5)

        # association des widgets aux fonctions
        boutonLancer.config(command=self.tirage) # appel "callback" (pas de parenthèses !)
        boutonQuitter.config(command=self.destroy)  # idem

    # tire un entier au hasard et l'affiche dans self.__texteResultat
    def tirage(self):
        nb = randint(1, 100)
        self.__texteResultat.set('Nombre : ' + str(nb))


if __name__ == '__main__':
    app = FenPrincipale()
    app.mainloop()
