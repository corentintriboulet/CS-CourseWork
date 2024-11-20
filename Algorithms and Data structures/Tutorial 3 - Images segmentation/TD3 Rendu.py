from PIL import Image
from math import sqrt,log10

im = Image.open("lyon.png")

px = im.load()
W,H = im.size
print("largeur et hauteur",W,H)
liste=[]


def peindre(matrice,x,y,w,h,r,g,b):

    for i in range(w):
        for j in range(h):
            matrice[x+i,y+j] = (int(r),int(g),int(b))


def moyenne(matrice,x,y,w,h):
    sr, sg, sb = 0, 0, 0
    for i in range(w):
        for j in range(h):
            r,g,b = matrice[x+i, y+j]
            sr += r
            sg += g
            sb += b
    n = w*h
    return sr/n, sg/n, sb/n

def ecart_type(matrice,x,y,w,h):
    sr, sg, sb = 0, 0, 0
    scr, scg, scb = 0, 0, 0
    for i in range(w):
        for j in range(h):
            r,g,b = matrice[x+i, y+j]
            sr += r
            sg += g
            sb += b
            scr += r**2
            scg += g**2
            scb += b**2

    n = w*h
    return sqrt(scr/n - (sr/n)**2), sqrt(scg/n - (sg/n)**2), sqrt(scb/n - (sb/n)**2)

def est_homogene(matrice,x,y,w,h,seuil):
    ecr, ecg, ecb = ecart_type(matrice,x,y,w,h)
    return ecr <= seuil and ecg <= seuil and ecb <= seuil

def est_homogene2(matrice,x,y,w,h,seuil_couleur,seuil_lum): #nouvelle fonction homogène
    ecr, ecg, ecb = ecart_type(matrice,x,y,w,h)
    X= 0.2126*ecr + 0.7152*ecg + 0.0722*ecb
    return ecr <= seuil_couleur and ecg <= seuil_couleur and ecb <= seuil_couleur and X<=seuil_lum

def partition(x,y,w,h):
    w2 = w//2
    h2 = h//2
    return (
        (x,y,w2,h2) if w2 and h2 >=1 else None,
        (x+w2,y,w-w2,h2) if (w-w2) and h2 >=1 else None,
        (x,y+h2,w2,h-h2) if w2 and (h-h2) >=1 else None,
        (x+w2,y+h2,w-w2,h-h2) if (w-w2) and (h-h2) >=1 else None
        )

class Noeud():
    def __init__(self,x,y,w,h,r,g,b):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.g = g
        self.b = b



    def __str__(self,prefix=""):
        # if len(prefix) > 4:
        #     return ""
        return "\n".join((f"{prefix}({self.x},{self.y}) enfants :",
                    self.hg.__str__(prefix+"  ") if self.get_hg() !=None else prefix+ "  None",
                    self.hd.__str__(prefix+"  ") if self.get_hd() !=None else prefix+ "  None",
                    self.bg.__str__(prefix+"  ") if self.get_bg() !=None else prefix+ "  None",
                    self.bd.__str__(prefix+"  ") if self.get_bd() !=None else prefix+ "  None",
                ))



def compter(n):
    if n == None:
        return 0

    else:
        return 1 + compter(n.get_hg()) + compter(n.get_hd())+ compter(n.get_bg()) + compter(n.get_bd())

def peindre_arbre(matrice,l,i):
    if l==[]:
        return
    if l[i] == None:
        return
    if not len(l)<4*i+4:

        if l[4*i+1] == l[4*i+2] == l[4*i+3] == l[4*i+4] == None:
            n=l[i]
            peindre(n.x,n.y,n.w,n.h,round(n.r),round(n.g),round(n.b))
        else:
            peindre_arbre(matrice,l,4*i+1)
            peindre_arbre(matrice,l,4*i+2)
            peindre_arbre(matrice,l,4*i+3)
            peindre_arbre(matrice,l,4*i+4)


def a_fils(matrice,x,y,l,h,seuil_couleur,seuil_lum):
    a=False
    if h>1 and l>1:
        if est_homogene2(matrice,x,y,l,h,seuil_couleur,seuil_lum)==False :
            a=True
    return(a)

def ajout_fils(matrice,dico,indice,seuil_couleur,seuil_lum):
    if indice in dico:
        if a_fils(matrice,*dico[indice],seuil_couleur,seuil_lum):
            hg,hd,bg,bd=partition(*dico[indice])
            dico[4*indice+1]=hg; dico[4*indice+2]=hd; dico[4*indice+3]=bg; dico[4*indice+4]=bd


def arbre(matrice,seuil_couleur,seuil_lum,x=0,y=0,l=W,h=H):
    dico={0:[x,y,l,h]}  #dictionnaire
    indice=0
    while indice<=4*len(dico)+4:
        ajout_fils(matrice,dico,indice,seuil_couleur,seuil_lum)
        indice=indice+1
    return(dico)

def colorie(matrice,dico,seuil_couleur,seuil_lum):
    for indice in dico:
        if a_fils(matrice,*dico[indice],seuil_couleur,seuil_lum)==False:
            r,g,b=moyenne(matrice,*dico[indice])
            peindre(matrice,*dico[indice],r,g,b)


def err_quadra(matrice0,matrice,W,H):
    err=0
    for i in range(W):
        for j in range(H):
            for l in range(3):
                err=err+(matrice[i][j][l]-matrice0[i][j][l])**2
    return(err)

def PSNR(matrice,seuil_couleur,seuil_lum):
    matrice0=matrice
    W,L=im.size
    Arbre=arbre(matrice,seuil_couleur,seuil_lum)
    colorie(matrice,Arbre,seuil_couleur,seuil_lum)
    return(20*log10(255)-10*log10(err_quadra(matrice0,matrice,W,L)/(3*W*L)))

# peindre(10,10,50,40,255,0,0)

# mr, mg, mb = moyenne(0,0,W,H)
# print(mr, mg, mb)

# mr, mg, mb = moyenne(0,0,10,10)
# print(mr, mg, mb)

# ecr, ecg, ecb = ecart_type(0,0,W,H)
# print(ecr, ecg, ecb)

# ecr, ecg, ecb = ecart_type(0,0,10,10)
# print(ecr, ecg, ecb)


# print(compter(racine))

#print(PSNR(racine,50,50))
#PSNR(px,50,50)


racine=[Noeud(0,0,4,4,128,128,128),Noeud(0,0,2,2,255,255,255),Noeud(2,0,4,2,128,128,128),Noeud(0,2,2,4,0,0,0),Noeud(2,2,4,4,128,128,128),None,None,None,None,Noeud(2,0,3,1,128,128,128),Noeud(3,0,4,1,0,0,0),Noeud(2,1,3,2,0,0,0),Noeud(3,1,4,2,128,128,128),None,None,None,None,Noeud(2,2,3,3,255,255,255),Noeud(3,2,4,3,255,255,255),Noeud(2,3,3,4,128,128,128),Noeud(3,3,4,4,128,128,128)]

def trace_memoire_temps(matrice):
    Duree=[]
    Seuil=[]

    for seuil in range(10,90,5):
        deb=time.time()
        dictio=arbre(matrice_px,seuil,255)
        fin=time.time()
        Duree.append(fin-deb)


        Seuil.append(seuil)
    plt.plot(Seuil,Duree,'bo')
    plt.title('Durée en fonction de la précision')
    plt.show()

if __name__ == '__main__':#execute le programme principal
    matrice_px=im.load()
    dictio=arbre(matrice_px,50,10)
    colorie(matrice_px,dictio,50,10)
    im.show()


