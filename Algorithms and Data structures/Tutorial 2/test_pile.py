from Pile import *

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

    p = Pile()
    for d in data:
        p.ajoute(d)

    e = p.supprime()
    assert(e['nom'] == "Arthaud" and e['prenom'] == "Nathalie")
