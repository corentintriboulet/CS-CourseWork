##Livre
class Livre:
    def __init__(self, nom, t, num, nbe ):
        self.__nom_auteur=nom
        self.__titre=t
        self.__numero=num
        self.__nb_exemplaire=nbe

    def __str__(self):
        S =  'Nom de l auteur: '               + self.__nom_auteur         + '\n'
        S += 'Titre: '                         + self.__titre              + '\n'
        S += 'Numéro : '                       + str(self.__numero)        + '\n'
        S += 'Nombre d exemplaires restants: ' + str(self.__nb_exemplaire) + '\n'
        return S

    def get_numero(self):
        return self.__numero

    def get_nb_exemplaire(self):
        return self.__nb_exemplaire

    def retirer_exemplaire(self):
        if self.__nb_exemplaire==0:
            raise ValueError
        self.__nb_exemplaire-=1

    def rendre_exemplaire(self):
        self.__nb_exemplaire+=1

if __name__ == '__main__':

    # Des livres
    B1 = Livre('Le Père Goriot',  'Honoré de Balzac',         1, 101)
    B2 = Livre("Léon l'Africain", 'Amin Maalouf',             2, 102)
    B3 = Livre('Le Petit Prince', 'Antoine de Saint-Éxupery', 3, 103)
    B4 = Livre("L'Étranger",      'Albert Camus',             4, 104)



