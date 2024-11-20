##TD1: Algorythme et structure
import math
import random
import numpy.random as rd

def pair_impair():
    a=int(input('saisir un entier: '))
    if a%2==0:
        print(a, 'est pair')
    else:
        print(a, 'est impair')

def quadratique(a,b,c):
    if ( a == 0 ) :
        if ( b != 0) :
            print ( "Pas quad ratique : ra cine simple x = ",-c/b)
        else :
            print ( " une blague ! " )
    else :
        delta=b*b-4*a*c
        if delta<0:
            print("pas de racines reelles")
        else:
            assert a!=0
            if delta>0:
                x1 = (-b+math.sqrt(delta))/(2*a)
                x2=(-b-math.sqrt(delta))/(2*a)
                print("x1= ",x1)
                print("x2= ",x2)
            else:
                x1 = x2 = -b/(2*a)
                print("racine double = ",x1)


echantillon=[random.gauss(16,2) for n in range(100)]

def moyenne(l):
    return sum(l)/len(l)

def ecart_type(l):
    esperance=moyenne(l)
    variance=moyenne([(i-esperance)**2 for i in l])
    return math.sqrt(variance)

def ecart_type2(l):
    return math.sqrt(abs(1/len(l)*sum([i**2 for i in l])-moyenne(l)**2))

def convertir(S):
    l_int=[]
    if S.isdigit():
        for i in S:
            l_int.append(int(i))
        return l_int
    else:
        for i in range(len(S)):
            if is_float(S[i]):
                l_int.append(int(S[i]))
        return l_int

def is_float ( value ) :
    try :
        float ( value )
        return True
    except :
        return False

def convertir2r(S):
    l_float=[]
    if S.isdigit():
        for i in S:
            l_float.append(float(i))
        return l_float
    else:
        for i in range(len(S)):
            if is_float(S[i]):
                l_int.append(float(S[i]))
        return l_float

def moyennes(V1):
    l=len(V1)
    V2=[None]*l
    for i in range(l):
        V2[i]=sum(V1[:i+1])/(i+1)
    return V2
def meth_em(l,l_id_manquant):
    moy_i=0;sigma=1;k=1
    if l_id_manquant==[]:
        return k,l
    else:
        for i in l_id_manquant:
            l[i]=moy_i
        moy_j=moyenne(l)
        while abs(moy_i-moy_j)>0.001:
            moy_i=moy_j
            for i in l_id_manquant:
                l[i]=moy_i
            moy_j=moyenne(l)
            k+=1
        return k,l

def suppr_sans_changer_ordre(l):
    liste=[l[0]]
    for i in l:
        if i not in liste:
            liste. append(i)
    return liste

def Scinder_une_liste():
    N=random.randint(10,100)
    L=rd.randint(2,N*4,(N))
    i=0;L1=[];L2=[]
    while i!=N:
        if i==N-1:
            L2.append(L[i])
            i+=1
        elif L[i]<=L[i+1]:
            L1.append(L[i]);L1.append(L[i+1]);
            i=i+2
        else:
            L2.append(L[i])
            i+=1
    return N,L,L1,L2

def tableau_sqrt(N):
    for i in range(N):
        print('{0:2d} : {1:3d} : {2:4.3f}'.format(i, i**2, math.sqrt(i)))

def aprox_e(n):
    S=0
    for i in range(n):
        S+=1/math.factorial(i)
    return abs(S-math.exp(1))

def nombre_premier(n):
    if n==1 or n==2:
        return True
    else:
        for i in range(2,int(n//2)+1):
            if n%i==0:
                return False
        return True

def diviseur_propre(n):
    l=[]
    if n==1 :
        return l
    if n==2:
        return l+[2]

    for i in range(2,int(n//2)+1):
        if n%i==0:
            l.append(i)
    if l==[]:
        return n,'est premier'
    return l

def decompte_voy_cons(ph):
    voyelles= 'aeiouy';tot_voy=0
    consonnes='zrtpqsdfghjklmwxcvbn';tot_cons=0
    for v  in voyelles :
        tot_voy += ph.lower().count(v)
    for c in consonnes:
        tot_cons += ph.lower().count(c)
    return 'Les nombres de consonnes est {} et celui des voyelles est {}'.format(tot_cons,tot_voy)

def nb_facon_2de(n):
    l=[]
    for i in range(1,7):
        for j in range(1,7):
            if i+j==n:
                l.append([i,j])
    return len(l),l

def nb_facon_3de(n):
    l=[]
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                if i+j+k==n:
                    l.append([i,j,k])
    return len(l),l






