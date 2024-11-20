##Bibiliotheque
from Lecteur import Lecteur
from Livre import Livre

class Bibliotheque:
    def __init__(self, nom ,Liste_lecteur,Liste_livre):
        self.__nom=nom
        self.__liste_lecteur=list(Liste_lecteur)
        self.__liste_livre=list(Liste_livre)

    def __str__(self):
        S = ' Nom de la bibliotheque: ' + self.__nom + '\n'
        return S

    def get_nom(self):
        return self.__nom

    def __str__(self):
        S = 'Nom de la bibliotheque: ' + self.__nom + '\n'+'\n'+'\n'
        S+= 'LECTEUR:'+'\n'+'\n'
        for i in range(len(B.get_liste_lecteur())):
            S += ' Nom : '     + B.get_liste_lecteur()[i][0] + '\n'
            S += ' Adresse : ' + B.get_liste_lecteur()[i][1] + '\n'
            S += ' Numéro : '  + str(B.get_liste_lecteur()[i][2]) + '\n'+'\n'
        S+='\n'
        S+= 'LIVRE:'+'\n'+'\n'
        for i in range(len(B.get_liste_livre())):
            S += ' Nom de l auteur: '              + B.get_liste_livre()[i][0] + '\n'
            S += ' Titre: '                        + B.get_liste_livre()[i][1] + '\n'
            S += ' Numéro : '                      + str(B.get_liste_livre()[i][2]) + '\n'
            S += 'Nombre d exemplaires restants: ' + str(B.get_liste_livre()[i][3]) + '\n'+'\n'
        return S

##Livre
    def get_liste_livre(self):
        return self.__liste_livre

    def get_len_livre(self):
        return len(B.get_liste_livre())

    def ajouter_livre(self,nom,t,num,nbe):
        B.get_liste_livre().append([ nom, t, num,nbe])

    def chercher_livre_nom(self,nom):
        a=0
        for i in range(B.get_len_livre()):
            if nom==str(B.get_liste_livre()[i][0]):
                a=1
                S += 'Nom de l auteur: '               + B.get_liste_livre()[i][0]      + '\n'
                S += 'Titre: '                         + B.get_liste_livre()[i][1]      + '\n'
                S += 'Numéro : '                       + str(B.get_liste_livre()[i][2]) + '\n'
                S += 'Nombre d exemplaires restants: ' + str(B.get_liste_livre()[i][3]) + '\n'+'\n'
                return print(S)
        if a==0:
            return 'Aucun livre ne possede cet auteur'

    def chercher_livre_titre(self,t):
        a=0
        for i in range(B.get_len_livre()):
            if nom==str(B.get_liste_livre()[i][1]):
                a=1
                S += ' Nom de l auteur: '              + B.get_liste_livre()[i][0] + '\n'
                S += ' Titre: '                        + B.get_liste_livre()[i][1] + '\n'
                S += ' Numéro : '                      + str(B.get_liste_livre()[i][2]) + '\n'
                S += 'Nombre d exemplaires restants: ' + str(B.get_liste_livre()[i][3]) + '\n'+'\n'
                return print(S)
        if a==0:
            return 'Aucun livre ne possede ce titre'

    def chercher_livre_num(self,num):
        a=0
        for i in range(B.get_len_livre()):
            if nom==str(B.get_liste_livre()[i][2]):
                a=1
                S += ' Nom de l auteur: '              + B.get_liste_livre()[i][0] + '\n'
                S += ' Titre: '                        + B.get_liste_livre()[i][1] + '\n'
                S += ' Numéro : '                      + str(B.get_liste_livre()[i][2]) + '\n'
                S += 'Nombre d exemplaires restants: ' + str(B.get_liste_livre()[i][3]) + '\n'+'\n'
                return print(S)
        if a==0:
            return 'Aucun livre ne possede ce numero'

##Lecteur
    def get_liste_lecteur(self):
            return self.__liste_lecteur

    def recherche_lecteur(self,num):
            if len(B.get_liste_lecteur())<num:
                return 'Ce numero n existe pas'
            else:
                return Lecteur(Liste_lecteur(num))

    def ajouter_lecteur(self,nom,a,num):
        B.get_liste_lecteur().append([nom,a,num])

    def supprimer_lecteur(self,num):
        longueur=B.get_len_lecteur()
        if longueur<num:
            raise ValueError
        else:
            B.get_liste_lecteur().pop(num-1)

    def get_len_lecteur(self):
        return len(B.get_liste_lecteur())

    def chercher_lecteur_num(self,num):
        a=0
        for i in range(B.get_len_lecteur()):
            if num==B.get_liste_lecteur()[i][2]:
                a=1
                S =  ' Nom : '     + B.get_liste_lecteur()[i][0] + '\n'
                S += ' Adresse : ' + B.get_liste_lecteur()[i][1] + '\n'
                S += ' Numéro : '  + str(B.get_liste_lecteur()[i][2]) + '\n'+'\n'

                return print(S)
        if a==0:
            return 'Personne ne possede ce numero '

    def chercher_lecteur_nom(self,nom):
        a=0
        for i in range(B.get_len_lecteur()):
            if nom==str(B.get_liste_lecteur()[i][0]):
                a=1
                S =  ' Nom : '     + B.get_liste_lecteur()[i][0] + '\n'
                S += ' Adresse : ' + B.get_liste_lecteur()[i][1] + '\n'
                S += ' Numéro : '  + str(B.get_liste_lecteur()[i][2]) + '\n'+'\n'

                return print(S)
        if a==0:
            return 'Personne ne possede ce nom'

if __name__ == '__main__':
    B=Bibliotheque('Michel Serre',[],[])

    B.ajouter_livre('Le Père Goriot',  'Honoré de Balzac',         1, 101)
    B.ajouter_livre("Léon l'Africain", 'Amin Maalouf',             2, 102)
    B.ajouter_livre('Le Petit Prince', 'Antoine de Saint-Éxupery', 3, 103)
    B.ajouter_livre("L'Étranger",      'Albert Camus',             4, 104)

    B.ajouter_lecteur('Mzai Ahmed',        'Boulevard de la Paix', 1)
    B.ajouter_lecteur('Xu John',           'Rue de la Gare',       2)
    B.ajouter_lecteur('Levgueni Dimitri',  'Impasse La Fayette',   3)
    B.ajouter_lecteur('Rodriguez Alfonso', 'Rue du Stade',         4)







