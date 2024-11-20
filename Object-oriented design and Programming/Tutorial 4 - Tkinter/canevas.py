from tkinter import *
from formes import *
from tkinter.colorchooser import askcolor

class ZoneAffichage(Canvas):
    def __init__(self, parent, largeur, hauteur):
        Canvas.__init__(self, parent, width=largeur, height=hauteur)

        self.type_forme=0
        self.liste_r=[]
        self.liste_e=[]
        self.color = "blue"

    def creer_forme(self,event):
        x,y=event.x,event.y
        if self.type_forme==1 :#rectangle
            f=Rectangle(self,x,y,100,100,self.color)
            self.liste_r.append(f)
        elif self.type_forme==2: #ellipse
            f=Ellipse(self,x,y,20,30,self.color)
            self.liste_e.append(f)

    def suppr_forme(self,event):
        x,y=event.x,event.y
        for R in self.liste_r:
            if R.contient_point(x,y):
                R.effacer()
        for E in self.liste_e:
            if E.contient_point(x,y):
                E.effacer()

    def change_color(self):
        C = askcolor(title="Choisis ta couleur")
        self.color=C[1]




    def change_type_rect(self):#type_forme =1
        self.type_forme=1
        print("Rectangle")

    def change_type_ellipse(self):
        self.type_forme=2
        print("Ellipse")



class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.configure(bg="grey")
        self.title('Dessin de formes')
        self.geometry("400x400+200+200")

        # Création d'un widget Canvas (zone graphique)
        Frame_menu = Frame(self, width = 5, bg = 'white',relief=GROOVE)
        Frame_menu.pack(side=TOP,padx=5,pady=5)
        self.Frame_dessin = ZoneAffichage(self,600,400)
        self.Frame_dessin.pack(side=TOP, padx=5, pady=5)
        # Initialisation de l'arbre de scène
        boutonRectangle= Button(Frame_menu,text="Rectangle")
        boutonRectangle.pack(side=LEFT, padx=5, pady=5)
        boutonEllipse= Button(Frame_menu,text="Ellipse")
        boutonEllipse.pack(side=LEFT, padx=5, pady=5)
        boutonCouleur= Button(Frame_menu,text="Couleur")
        boutonCouleur.pack(side=LEFT, padx=5, pady=5)
        boutonQuitter= Button(Frame_menu,text="Quitter")
        boutonQuitter.pack(side=LEFT, padx=5, pady=5)

        #Forme.__init__(self,Frame_dessin,0,0)


        #event
        #Frame_dessin.bind("<ButtonRelease-1>",ZoneAffichage.clic)
        #Frame_dessin.bind("<ButtonRelease-1>",Rectangle(Frame_dessin,0,0,20,20,"blue"))

        #commande des boutons
        boutonQuitter.config(command=self.destroy)
        boutonRectangle.config(command=self.Frame_dessin.change_type_rect)
        boutonEllipse.config(command=self.Frame_dessin.change_type_ellipse)
        boutonCouleur.config(command=self.Frame_dessin.change_color)

        self.Frame_dessin.bind("<ButtonRelease-1>",self.Frame_dessin.creer_forme)
        self.Frame_dessin.bind("<Control-ButtonRelease-1>",self.Frame_dessin.suppr_forme)

def clic(event):
    X=event.x
    Y=event.y
    return[X,Y]

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


if __name__ == "__main__":
    fen = FenPrincipale()
    fen.mainloop()

















