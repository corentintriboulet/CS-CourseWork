##Emprunt
from Lecteur import Lecteur
from Livre import Livre

class Emprunt:
    def __init__(self, num_lecteur,num_livre):
        self.__num_lecteur=numero_lecteur
        =numero_livre
        self.__date_emprunt=date.isoformat(date.today())

    def get_num_lecteur(self):
        return self.__num_lecteur

    def get_num_livre(self):
        return self.__num_livre




    def __str__(self):
        S = 'Le lecteur suivant:'+ self. + '\n'
        S += ' a emprunté le livre suivant: ' + B.chercher_livre_num(self.__num_livre)
        return S



if __name__ == '__main__':
 #Création d'un emprunt entre un lecteur et un livre
    E1 = Emprunt(1, 100)
    print('Emprunt --> ', E1)
    print("Num lecteur de l'emprunt : ", E1.get_numero_lecteur())
