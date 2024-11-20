labyrinthe = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

def affiche_labyrinthe(l):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        for row in l]))

def voisin(c,l):
    (x,y)=c
    return [(x+dx,y+dy) for dx,dy in[(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,-1)]
    if 0<=x+dx<len(l) and 0<=y+dy<len(l[0]) and l[x+dx][y+dy]==0]

def existe_chemin(c,l,passage):#renvoie None s'il n'y a pas de chemin et True sinon
    if c==(len(l)-1,len(l[0])-1):
        return True
    else:
        if c not in passage:
            passage.append(c)
        for cell in voisin(c,l):
            if cell not in passage:
                return existe_chemin(cell,l,passage)

def test_profondeur(c,l,passage):#True si le chemin existe, False sinon
    return existe_chemin((0,0),labyrinthe,[])!=None

def test_profondeur_ite(l):
    passage=[]
    c=(0,0)
    voisin(c,l)
    pass

def heuristique(c1,c2):
    (x1,y1)=c1
    (x2,y2)=c2
    return abs(x1-x2)+abs(y1-y2)

def existe_chemin_it(l,c=(0,0)):
    file=[]
    file.append(c)
    visites=[]
    end=(len(l)-1,len(l[0])-1)
    while len(file)>0:
        courant=file.pop(0)
        vs=voisin(l,courant)
        for v in vs:
            if v not in visites:
                visites.append(v)
                file.append(v)
                if v==end:
                    return True







