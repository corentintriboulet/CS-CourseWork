##Lecteur
class Lecteur:
    def __init__(self, nom, a, num ):
        self.__nom=nom
        self.__numero=num
        self.__adresse=a

    def __str__(self):
        S = ' Nom : ' + self.__nom + '\n'
        S += ' Adresse : ' + self.__adresse + '\n'
        S += ' Numéro : ' + str(self.__numero) + '\n'
        return S



if __name__ == '__main__':

    # Des lecteurs
    L1 = Lecteur('Mzai Ahmed',        'Boulevard de la Paix', 1)
    L2 = Lecteur('Xu John',           'Rue de la Gare',       2)
    L3 = Lecteur('Levgueni Dimitri',  'Impasse La Fayette',   3)
    L4 = Lecteur('Rodriguez Alfonso', 'Rue du Stade',         4)

    Liste_lecteur=[['Mzai Ahmed','Boulevard de la Paix', 1],['Xu John','Rue de la Gare',2],['Levgueni Dimitri','Impasse La Fayette',3],['Rodriguez Alfonso','Rue du Stade',4]]



