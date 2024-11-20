from tkinter import *
from tkinter.colorchooser import askcolor
import random
from formes import *
import numpy as np

class ZoneAffichage(Canvas):  #creation de la classe zone d'affichage
    def __init__(self, parent, largeur, hauteur):
        Canvas.__init__(self, parent, width=largeur, height=hauteur)


class MonBoutonLettre(Button): #creation de la classe bouton associé à la lettre
    def __init__(self,parent,fenetre,lettre):
        self.lettre = lettre
        self.bouton = Button(parent,text=self.lettre, width =5,command = self.cliquer)
        self.fenetrePrincipale = fenetre

    def cliquer(self):
        self.fenetrePrincipale.traitement(self.lettre)
        self.bouton.config(state = DISABLED) #on ne peut plus cliquer sur le bouton

class Joueur: #creation de la classe joueur
    def __init__(self,nom,score):
        self.nom=nom
        self.score=score
        self.parties=0

    #DESCRIPTION Joueur(Nom du joueur,[(1),(2)]
    #(1)= 'perdu' si la partie est perdue
    #   = nombre d'essais pour réussir
    #(2)= True si la partie est gagnée
    #   = False si la partie est perdue

    def get_nom(self):
        return(self.nom)

    def get_score(self):
        return(self.score)

    def get_parties(self):
        return(self.parties)

    def set_score(self,score):
        self.score = score

    def set_parties(self, parties):
        self.parties = parties

class Partie(Joueur):
    def __init__(self):
        self.ljoueur=[] #liste des joueurs

    def nouveaujoueur(self,nom,score):
        j=Joueur(nom,[score])
        self.ljoueur.append(j)
        j.set_parties(1) #nouvelle partie

    def nouvellepartie(self,nom,score):#on sait que le joueur a deja joué
        for j in self.ljoueur:
            if j.get_nom()==nom:
                j.score.append(score) #ajout du score
                nb_ancienne_parties=j.get_parties()
                j.set_parties(1+nb_ancienne_parties) #ajout de 1 du nombre de partie

    def get_ljoueur(self):
        return(self.ljoueur)



class FenPrincipale(Tk,Partie,ZoneAffichage): #fenêtre principale, celle qui s'ouvre en première
    def __init__(self):
        Partie.__init__(self)
        Tk.__init__(self)

        self.title('Jeu du pendu')
        self.geometry("800x600+200+200")
        self.__couleur_rectancle="white"
        self.couleur_ZoneAffichage = "black"
        self.couleur_clavier='white'
        self.couleur_background='white'
        self.configure(background=self.couleur_background)
        self.__liste_event=[] #liste qui retrace les évènements
        self.ListeForme=[[ 50,  270, 200,  26, self.__couleur_rectancle],
        [ 87,   83,  26, 200, self.__couleur_rectancle],
        [ 87,   70, 150,  26, self.__couleur_rectancle],
        [183,   67,  10,  40, self.__couleur_rectancle],
        [ 188, 120,  20,  20, self.__couleur_rectancle],
        [ 175, 143,  26,  60, self.__couleur_rectancle],
        [ 133, 150,  40,  10, self.__couleur_rectancle],
        [ 203, 150,  40,  10, self.__couleur_rectancle],
        [ 175, 205,  10,  40, self.__couleur_rectancle],
        [ 191, 205,  10,  40, self.__couleur_rectancle]]#liste des formes qui composent la personne du pendu


        #Barre d'outils
        Barre_doutils=Frame(self)
        Barre_doutils.pack(side=TOP)
        Barre_doutils.configure(bg='white')

        #bouton quitter
        boutonQuitter=Button(Barre_doutils,text=" ❌ ",bg='red' )
        boutonQuitter.pack(side=RIGHT, padx=5, pady=5)

        #bouton scores
        boutonScores=Button(Barre_doutils,text=" Scores ",bg='yellow' )
        boutonScores.pack(side=RIGHT, padx=5, pady=5)

        #bouton nouvelle partie
        boutonNouvellePartie=Button(Barre_doutils,text=" ➕ ",bg='green')
        boutonNouvellePartie.pack(side=RIGHT, padx=5, pady=5)

        #Menu pour changer la couleur des formes du pendu
        boutonCouleur=Menubutton(Barre_doutils,text='Choisir une couleur | ✒️ ',bg='white')
        boutonCouleur.pack(side=RIGHT, padx=5, pady=5)
        menuDeroulantCouleur=Menu(boutonCouleur, tearoff = 0)
        menuDeroulantCouleur.add_command(label='Couleur du pendu', command=self.changer_couleur_rectangle)
        menuDeroulantCouleur.add_command(label="Couleur de la zone d'affichage", command=self.changer_couleur_ZoneAffichage)
        menuDeroulantCouleur.add_command(label='Couleur du clavier', command=self.changer_couleur_clavier)
        menuDeroulantCouleur.add_command(label="Couleur de l'arrière plan", command=self.changer_couleur_background)

        #bouton retour en arrière
        boutonUndo=Button(Barre_doutils,text=' ↩️ ',bg='blue')
        boutonUndo.pack(side=RIGHT, padx=5, pady=5)


        #Zone d'affichage du pendu
        self.Frame_dessin = ZoneAffichage(self,300,300)
        self.Frame_dessin.pack(side=TOP, padx=5, pady=5)
        self.Frame_dessin.configure(bg=self.couleur_ZoneAffichage )

        #Mot à decouvrir
        ZoneMot=Frame(self)
        self.labelMot = StringVar()
        self.labelMot.set("Mot:")
        lmot=Label(self,textvariable=self.labelMot)
        lmot.pack(side=TOP)

        #Clavier
        ZoneClavier=Frame(self)
        ZoneClavier.configure(bg=self.couleur_clavier,width=200, height=50)
        ZoneClavier.pack(side=TOP, padx=5, pady=5)
        self.lbouton = [] #liste qui contient tout les boutons
        #création du clavier
        for i in range(26):
            self.lbouton.append(MonBoutonLettre(ZoneClavier,self,chr(ord('A')+i)))
        for i in range(7):
            self.lbouton[i].bouton.grid(row=1, column=i+1,ipadx=20, ipady=5,padx=2, pady=2)
        for i in range (7,14):
            self.lbouton[i].bouton.grid(row=2, column=i-6,ipadx=20, ipady=5,padx=2, pady=2)
        for i in range (14,21):
            self.lbouton[i].bouton.grid(row=3, column=i-13,ipadx=20, ipady=5,padx=2, pady=2)
        for i in range(21,26):
            self.lbouton[i].bouton.grid(row=4, column=i-19,ipadx=20, ipady=5,padx=2, pady=2)
        for i in range(26):
            self.lbouton[i].bouton.config(state=DISABLED)

        #Configuration des boutons
        boutonQuitter.config(command=self.destroy)
        boutonScores.config(command=self.afficheTableauScore)
        boutonNouvellePartie.config(command=self.newgame)
        boutonCouleur.configure(menu=menuDeroulantCouleur)
        boutonUndo.config(command=self.undo)
        self.chargeMots() #appel de la fonction pour importer les mots

        if len(self.__liste_event)!=0: #si aucun événements a été enregistré, on ne peut pas cliquer sur retour en arrière
            boutonUndo.config(state=NORMAL)

    def set_couleur_rectangle(self,couleur):
        self.__couleur_rectancle=couleur

    def set_couleur_ZoneAffichage(self,couleur):
        self.couleur_ZoneAffichage  = couleur

    def set_couleur_clavier(self,couleur):
        self.couleur_clavier =couleur

    def set_couleur_background(self,couleur):
        self.couleur_background =couleur

    def nouveauMot(self): #choisis aléatoirement un mot parmi la liste du fichier
        return(random.choice(self.__mots))


    def chargeMots(self): #importe la liste de mots
        f = open('mots.txt', 'r')
        s = f.read()
        self.__mots = s.split('\n')
        f.close()

    def newgame(self): #créé une nouvelle partie
        for b in self.lbouton:
           b.bouton.config(state=NORMAL)
        self.nbcoupsmanques =0 #initialisation des coups manqués
        self.__mot=self.nouveauMot() #choix d'un nouveau mot
        self.mot_cache='*'*len(list(self.__mot))
        self.labelMot.set('Mot : '+self.mot_cache) #mot caché par des *
        self.Frame_dessin.delete(ALL)
        #for i in range(10):
            #self.Frame_dessin.delete(i)
        self.nouvellefenetre()


    def traitement(self,lettre): #fonction appelée lorsqu'on clique sur une lettre (bouton)
        if lettre in self.__mot: #on verifie si la lettre demandee est dans le mot a decouvrir
            newmotcache=''
            for i in range(len(self.__mot)):
                if self.__mot[i] == lettre:
                    newmotcache+=lettre   #si c'est la bonne lettre
                else:
                    newmotcache+=self.mot_cache[i]
            if not '*' in newmotcache: #si il n'y a plus d'étoiles dans le mot caché
                self.finPartie(True)  #partie gagnée
            else: #on a trouve une lettre
                self.mot_cache = newmotcache
                self.labelMot.set('Mot : '+self.mot_cache+'\n'+"Bien joué!")
                self.__liste_event.append([lettre,True])

        else:   #si on a manqué notre coup (ie la lettre n'est pas dans le mot)
            self.nbcoupsmanques  += 1
            if self.nbcoupsmanques == 10: #A t-on épuisé le nombre de coups ?
                self.finPartie(False)  #partie perdue
                       #affichage du dernier morceau du pendu
            else:#on n'a pas trouve de lettre mais la partie n'est pas terminée
                self.generer()
                self.labelMot.set('Mot : '+self.mot_cache+'\n'+"Raté!")
                self.__liste_event.append([lettre,False])


        print(self.__liste_event)
        #print(self.mot_cache)

                #print("Vous avez essayé "+ str(self.nbcoupsmanques)+" fois") #affichage d'un morceau de plus du pendu

    def setState(self, s): #change l'état de l'item en l'état "s"
        self.__canevas.itemconfig(self._item, state=s)



    def affiche_rectangle_i(self,i): #affiche la i_ème forme
        self.Frame_dessin.create_rectangle(self.ListeForme[i][0], self.ListeForme[i][1],self.ListeForme[i][0]+self.ListeForme[i][2],self.ListeForme[i][3]+self.ListeForme[i][1],fill=self.ListeForme[i][4])

    def generer(self): #permet d'afficher la prochaine forme
        self.affiche_rectangle_i(self.nbcoupsmanques)
        #print("J'affiche le rectancle "+str(i)

    def finPartie(self,bool):#fonction qui s'execute en fin de partie
        score=None
        for b in self.lbouton:
            b.bouton.config(state=DISABLED)    #changement d'état des boutons
        if bool==True: #la partie est gagnée
            self.labelMot.set('Mot : '+self.__mot + '\n'+"Vous avez gagné!")
            score=self.nbcoupsmanques #nombre de coups pour gagner

        if bool==False: #la partie est perdue
            score='perdu'
            c=0
            for i in self.mot_cache:
                if i =='*':
                    c+=1
            self.labelMot.set('Mot : '+self.mot_cache + '\n'+"Vous avez perdu!"+'\n'+"Il restait "+str(c)+ " lettres à découvrir")

        bool=False
        for j in self.ljoueur:
            if self.__nom.get()==j.get_nom():
                bool=True

        if bool==True:#le joueur a déjà joué
            self.nouvellepartie(self.__nom.get(),score)

        else:
            self.nouveaujoueur(self.__nom.get(),score)


    def changer_couleur_rectangle(self): #change la couleur des formes qui vont être affichées à l'avenir
        C = askcolor(title="Choisis ta couleur")
        self.set_couleur_rectangle(C[1])

    def changer_couleur_ZoneAffichage(self): #change la couleur des formes qui vont être affichées à l'avenir
        C = askcolor(title="Choisis ta couleur")
        self.set_couleur_ZoneAffichage(C[1])

    def changer_couleur_clavier(self): #change la couleur d'arrière plan du clavier
        C = askcolor(title="Choisis ta couleur")
        self.set_couleur_clavier(C[1])

    def changer_couleur_background(self): #change la couleur d'arrière plan du clavier
        C = askcolor(title="Choisis ta couleur")
        self.set_couleur_background(C[1])

    def undo(self):  #qu'a ton fait au tour precedent ?
        num_bouton=ord(self.__liste_event[-1][0])-ord('A')
        self.lbouton[num_bouton].bouton.config(state=NORMAL) #changer l'état de la lettre
        if self.__liste_event[-1][1]==False: #on a raté le dernier coup
            self.Frame_dessin.delete(self.nbcoupsmanques) #retirer la forme du coup manque
            self.nbcoupsmanques-=1 #reset des coups manqués

        else: #on a trouver une lettre au dernier coup
            newmotcache=''
            for i in range(len(self.__mot)):
                #print(newmotcache)
                T=np.array(self.__liste_event) #convertion
                if self.__mot[i] in list(T[:-1,0]):#si c'est la bonne lettre (on vérifie dans les anciens coups)
                    newmotcache+=self.__mot[i]
                else:
                    newmotcache+='*'
            self.mot_cache = newmotcache
        self.labelMot.set('Mot : '+self.mot_cache+'\n'+"Vous avez annulé le coup précédent")
        self.__liste_event.pop() #on retire le dernier coup de la liste

    def nouvellefenetre(self): #créé la nouvelle fenetre
        self.__nom = StringVar()
        nouvellefen = Toplevel(fen)
        EmployeID=Label(nouvellefen, text="Nom :").pack(side=LEFT,ipadx=20,ipady=20,padx=2, pady=2)
        nomparticipant = Entry(nouvellefen,textvariable=self.__nom)
        nomparticipant.pack(side=LEFT,ipady=5,padx=20, pady=2)
        consigne=Label(nouvellefen,text="(Fermer la fenêtre après avoir renseigné votre nom)")
        consigne.pack(side=LEFT,ipady=5,padx=20, pady=2)


    def afficheTableauScore(self):
        fenScores=Toplevel(fen) #ouverture d'une fenêtre où l'on affiche les scores
        self.Tableau=[]
        nombre_parties_max=0
        nombre_joueur=len(self.ljoueur)

        for j in self.ljoueur:#determination du nombre maximal de partie de tous les joueurs
            if nombre_parties_max<len(j.get_score()):
                nombre_parties_max=len(j.get_score())

        #creation du Tableau en type tableau-liste
        for j in self.ljoueur:
            self.Tableau.append([j.get_nom()]+j.get_score()+[None]*(nombre_parties_max-len(j.get_score()))) #les cases None correspondent au fait que le joueur n'a pas encore joué cette partie

        #creation de chaque case du tableau
        Tab=np.array(self.Tableau)
        for i in range(nombre_joueur):
            for j in range(nombre_parties_max + 1):#on affiche le nom + les parties

                self.e = Label(fenScores, width=20, fg='grey',justify=CENTER,text=str(Tab[i,j]))#insertion du score dans le tableau
                self.e.grid(row=i+1, column=j+1,ipadx=5,ipady=5,padx=5,pady=5) #decalage à cause de l'indication


        #commentaires à ajouter en haut du tableau
        indication=Label(fenScores,text="Scores: nombres d'essais pour gagner OU mention perdu")
        indication.grid(row=0, column=0,ipady=5,padx=5, pady=2)
        nom_joueur=Label(fenScores,text="Nom des joueurs")
        nom_joueur.grid(row=0, column=1,ipady=5,padx=5, pady=2)

        for i in range(nombre_parties_max):#affichage des parties
                self.e = Label(fenScores, text='Partie ' + str(i+1))
                self.e.grid(row=0, column=i+2,ipadx=5,ipady=5,padx=5,pady=5) #decalage à cause de l'indication



if __name__ == '__main__':#execute le programme principal
	fen = FenPrincipale()
	fen.mainloop()



