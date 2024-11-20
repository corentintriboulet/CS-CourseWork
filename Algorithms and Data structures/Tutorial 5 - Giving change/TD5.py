##Glouton
def Monnaie_Gloutonne(S,M):
    Ti=[]
    T=[0]*len(S)
    M2=M
    while M2>0:
        i=len(S)-1
        v=S[-1]
        while S[i]>M2: #on selectionne toujours la plus grosse pièce
            i=i-1
        Ti.append([i,M2//S[i]])
        M2=M2%S[i]

    for element in Ti: #reconstituer T
        i=element[0]
        T[i]=element[1]
    Q=sum(T)
    return T,Q

def Monnaie_Gloutonne_limitee(S,D,M):
    #S liste des valeurs des pièces
    #D le nombre de pièces de chaque type
    #M la monnaie à rendre

    if len(S)!=len(D): #si les listes n'ont pas la même taille
        return ValueError
    Ti=[]
    T=[0]*len(S)
    M2=M
    i=len(S)-1
    while M2>0:
        if D==[0]*len(D):
            return "Il n'y a pas assez de pièces pour rendre la monnaie"
        while S[i]>M2 or D[i]==0:
            i=i-1

        N=M2//S[i]
        if D[i]<N: #verification du nombre de pièces disponible
            N=D[i]

        Ti.append([i,N]) #actualisation du portefeuille
        M2=M2-(S[i]*N)
        D[i]-=N

    for element in Ti: #reconstituer T
        i=element[0]
        T[i]=element[1]
    Q=sum(T)
    return print(" Portefeuille restant:",D,"\n Rendu de monnaie:",T,"\n Nombre de pieces rendues: ",Q)




def Monnaie_graphe(L,S,i=0,X=[]):#L=[M]
    n=len(S)
    if L[i] in S:
        return [L[i]]
    elif L[i]>0:

        e=1;k=i;l=1 #calcul de l'etage + longeur que doit avoir L
        while k!=0:
            e+=1
            k=int((k-1)/n)
            l+=n**e

        if len(L)<l:
            L+=[None]*n**e

        for j in range(n):
            L[n*i+1+j]=L[i]-S[j]
            Monnaie_graphe(L,S,n*i+1+j,X)
    if L[i]==0:
        T=[]
        while i!=0:
            j=int((i-1)/n)
            T.append(L[j]-L[i])
            i=j
            X.append(T)
    return X

def Monnaie_graphe2(L,S):#gestion des doublons
    X=Monnaie_graphe(L,S)
    Y=[]
    if len(X)>1:
        for e in X:
            e.sort()
    for e in X:
        if e not in Y and sum(e)==L[0]:
            Y.append(e)
    return Y

def chemin_court(L,S):
        Y=Monnaie_graphe2(L,S)
        longueur=1000;element=[]
        for e in Y:
            if len(e)<longueur:
                element=e
                longueur=len(e)

        return element
## Partie 3

def matrice(S):
    M=[]
    for i in range(len(S)) :
        L=[]
        for i in range(1,11):
            L.append(len(chemin_court([i,None],S)))
            print(len(chemin_court([i,None],S)))
        M.append(L)
    return M

def test(S,i):
    return len(chemin_court([i,None],S))
