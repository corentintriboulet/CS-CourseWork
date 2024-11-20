import numpy as np
from numpy import inf
##Deuxieme version

class Noeud :
    def __init__(self,M,parent):
        self.__val = M
        self.__fils = []
        self.__parent = parent

    def get_valeur(self):
        return(self.__val)

    def get_parent(self):
        return(self.__parent)

    def get_fils(self):
        return(self.__fils)

    def ajout_enfant(self,valeur):
        enfant = Noeud(valeur,self)
        self.__fils.append(enfant)

    def ajout_enfant_existant(self,enfant):
        self.__fils.append(enfant)

    def trouve_enfant(self,valeur):
        for i in self.__fils:
            if i.get_valeur()==valeur:
                return(True)
        return(False)


def monnaie_graphe(M,S):

        F = []
        T = 0
        racine = Noeud(M,None)
        A =[racine]
        F.append(racine)
        trouve = False
        while  F != []:
            Noeudm = F.pop(0)
            m = Noeudm.get_valeur()
            for i in S:
                indic = 0

                for noeud in A:
                    if noeud.trouve_enfant(m-i): #si le noeud existe deja
                        Noeudm.ajout_enfant_existant(noeud)
                        indic = 1
                if indic ==0:#si le noeud n'existe pas,on l'ajoute
                    new_noeud = Noeud(m-i,Noeudm)
                    Noeudm.ajout_enfant(new_noeud)
                    F.append(new_noeud)

                if m-i == 0:
                    trouve = True
                    break

            if trouve :
                break


        noeud = new_noeud
        branche = [noeud]

        while noeud != racine:
            parent = noeud.get_parent()
            branche.append(parent)
            noeud = parent

        montant = [n.get_valeur() for n in branche]

        montant = montant[::-1]
        pieces = []
        m1 = montant[0] #montant initial
        for i in range(1,len(montant)):
            m2 = montant[i]
            pieces.append(m1-m2)
            m1 = m2

        T = [0]*len(S)
        for p in pieces :
            i = S.index(p)
            T[i]+=1

        return(T)
## Partie 3

def matrice(S):
    M=[]
    for i in range(len(S)) :
        L=[]
        for j in range(1,11):
            L.append(sum(monnaie_graphe(j,S[:i+1])))
        M.append(L)
        print(L)

def matrice2(S,M): #avec retour des pièces consommées
    s=len(S)+1
    mat=np.zeros((s,M+1))
    for i in range(s):
        for m in range(M+1):

            if m==0:  #definition des bords
                mat[i][m]=0
            elif i==0:
                mat[i][m]=inf #inf correspond à l'infini
            else:
                a,b=inf,inf

                if m-S[i-1]>=0:
                    a=1+mat[i][m-S[i-1]]
                else:
                    a=inf

                if i>=1:
                    b=mat[i-1][m]
                else:
                    b=inf

                mat[i][m]=min(a,b)
    pieces=[]
    x=s-1;y=M #coordonnées dans le tableau
    m=M

    while m!=0:
        if y-S[x-1]<0:#si on sort du tableau
            x,y=x-1,y
        elif mat[x-1][y]<mat[x][y-S[x-1]]:#on ne consomme pas de pièce
            x,y=x-1,y
        else: #on consomme une pièce
            x,y=x,y-S[x-1]
            pieces.append(S[x-1])
            m-=S[x-1]

    return mat,pieces

def monnaie_dynamique_limite(S,B,M):#avec un nombre de pièces limitées
    #S = valeur des pièces
    #B = nombre de pièces
    #M = montant voulu

    s=len(S)+1
    mat=np.zeros((s,M+1))
    for i in range(s):
        for m in range(M+1):

            if m==0:  #definition des bords
                mat[i][m]=0
            elif i==0:
                mat[i][m]=inf #inf correspond à l'infini
            else:
                l=[]
                for j in range(B[i-1]+1):
                    if m-j*S[i-1]>=0:
                        l.append(j+mat[i-1][m-j*S[i-1]])#liste des Q_opt

                mat[i][m]=min(l)
    pieces=[]
    x=s-1;y=M #coordonnées dans le tableau
    m=M
    if mat[x][y]==inf:
        return print("Il n'est pas possible de rendre la monnaie")
    else:
        pieces.append(S[])
        for i in range(mat[x][y]-1):

        return mat,pieces


