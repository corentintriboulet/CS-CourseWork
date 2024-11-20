data = []
nb_ligne=-1
with open("etudiants.txt") as f:
    keys = None
    for line in f:
        nb_ligne+=1
        l = [w.strip() for w in line.split(';')]
        if keys is None:
            keys = l
        else:
            data.append(l)
moy=0
for i in range(nb_ligne):
    moy+=int(data[i][3])/nb_ligne

#print(moy)

class Pile:
    def __init__(self):
        self.__liste=[]

    def ajoute(self,a):
        self.__liste.append(a)

    def supprime(self):
        if self.est_vide():
            return "erreur liste vide"
        else:
            return self.__liste.pop()

    def est_vide(self):
        return self.__liste==[]

    def renvoie(self,fonction):
        for i in self.__liste:
            if fonction(i):
                return i
            else:
                return(None)




class File:
    def __init__(self):
        self.__liste=[]

    def ajoute(self,a):
        self.__liste.append(a)

    def est_vide(self):
        return self.__liste==[]

    def supprime(self):
        if self.__liste.est_vide():
            return "erreur liste vide"
        else:
            return self.__liste.pop(-1)

    def renvoie(self,fonction):
        for i in self.__liste:
            if fonction(i):
                return i
        return None
class Tas:
    def __init__(self):
        self.__liste=[]

    def ajoute(self,a):
        self.__liste.append(a)

    def est_vide(self):
        return self.__liste==[]

    def supprime(self):
        if self.__liste.est_vide():
            return "erreur liste vide"
        else:
            return self.__liste.pop(-1)
    def get_racine(self):
        return self.__liste[0]

    def get_parent(self,i):
        return self.__liste(int((i-1)/2))

    def get_fils_gauche(self,i):
        return [self.__liste[2*i+1],2*i+1]

    def get_fils_droit(self,i):
        return [self.__liste[2*i+2],2*i+2]

    def inserer(self,a):
        if self.__liste==[]:
            self.__liste.append(a)
        else:
            l=len(self.__liste)
            if self.get_fils_gauche(l)[0]<a:
                self.__liste.append(self.get_fils_gauche(l)[0])
                self.__liste[self.get_fils_gauche(l)[1]]=a
            else:
                self.__liste.append(a)


if __name__=="__main__":

    data = []

    with open("etudiants.txt") as f:
        keys = None
        for line in f:
            l = [w.strip() for w in line.split(';')]
            if keys is None:
                keys = l
            else:
                data.append({k:v for k, v in zip(keys, l)})

    tas = Tas()

    for d in data:
        tas.inserer(int(d['moyenne']))
        print(int(d['moyenne']))

    r = tas.get_racine()
    fg, fg_i = tas.get_fils_gauche(0)
    ffg, ffg_i = tas.get_fils_droit(0)

    assert(r == 19 and fg == 14 and ffg == 16)

