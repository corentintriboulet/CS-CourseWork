##Hotellerie
import sqlite3
import matplotlib.pyplot as plt
import numpy             as np
from datetime import date

class HotelDB:
	def __init__(self, fichier):
		self.__conn = sqlite3.connect(fichier)
		self.__curseur = self.__conn.cursor()

	def get_name_hotel_etoile(self,nbEtoiles):
	#recupere le nom des hotels avec le nombre d'étoile demandé
		try:
			if nbEtoiles<=0:
				print("Nombre d'étoiles negatifs")
				raise ValueError
			self.__curseur.execute("SELECT nom FROM hotel WHERE etoiles =="+ str(nbEtoiles))
		except Exception:
			print('Une erreur a été relevée')
		else:
			return self.__curseur.fetchall()

	def __del__ (self):  #fonction appellée pour fermer le fichier sql
		self.__conn.close()


	def ajouter_client(self,prenom,nom):
		# ajoute un client s'il n'est pas présent dans la base
		curseur=self.__curseur
		try:
			curseur.execute(f"SELECT numclient FROM client WHERE nom='{nom}' and prenom='{prenom}'")
		except Exception:
			print('Une erreur a été relevée')
		liste=curseur.fetchall()
		if len(liste)!=0:
			print( "Le client existe deja. Son numéro est le " + str(liste[0][0]) +".")
		else:
			curseur.execute(f"INSERT INTO client(nom,prenom) VALUES ('{nom}','{prenom}')")
			print("Son numéro est le "+ str(curseur.lastrowid) + ".")
		self.__conn.comit()
		self.__conn.close()

	def prix_moyen_hotel(self,num):#renvoie le prix moyen d'une nuit pour un hotel donné (par son numéro) #Ce programme permettra de calculer la moyenne totale
		curseur=self.__curseur
		try:
			if type(num)!=int:
				raise TypeError
			curseur.execute(f"SELECT AVG(prixnuitht) FROM chambre WHERE numhotel='{num}' ")
		except Exception:
			print('Une erreur a été relevée')
		return curseur.fetchall()[0][0]

	def prix_hotel(self,num):#renvoie la liste de tous les prix d'un hotel donné (par son numéro)
		curseur=self.__curseur
		try:
			if type(num)!=int:
				raise TypeError
			curseur.execute(f"SELECT prixnuitht FROM chambre WHERE numhotel='{num}' ")
		except Exception:
			print('Une erreur a été relevée')
		else:
			return [l[0] for l in curseur.fetchall()]

	def liste_nom_hotel(self):
		curseur=self.__curseur
		try:
			curseur.execute("SELECT nom FROM hotel")
		except Exception:
			print('Une erreur a été relevée')
		return curseur.fetchall()

	def dates(self,num_resa): #renvoie les dates d'arrivée et de départ d'une réservation donnée par son numéro
		curseur=self.__curseur
		try:
			if type(num_resa)!=int:
				raise TypeError
			curseur.execute(f"SELECT datearrivee,datedepart FROM reservation WHERE numresa='{num_resa}' ")
		except Exception:
			print('Une erreur a été relevée')
		else:
			return curseur.fetchall()

	def liste_resa(self):#renvoie la liste des réservations (permet ensuite de connaître le nombre total de réservation)
		curseur=self.__curseur
		try:
			curseur.execute("SELECT numresa FROM reservation")
		except Exception:
			print('Une erreur a été relevée')
		return curseur.fetchall()

if __name__ == '__main__':
	aHotelDB = HotelDB('hotellerie.db')
	nbEtoiles = 2
	resultat = aHotelDB.get_name_hotel_etoile(nbEtoiles)
	#print("Liste des noms d'hotel", nbEtoiles, "étoiles : ", resultat)

	#id= aHotelDB.ajouter_client('Marcel','Dupont')
	#print('id client:',id)

	#prix_avg=aHotelDB.prix_moyen_hotel(1)
	#print("liste prix moyen: ", prix_avg)



def histogramme_prix_moyen_chambre():#affiche l'histogramme
	Prix_Moyen=[]
	Prix=[]
	Nom_Hotel=[]
	l=len(aHotelDB.liste_nom_hotel())

	for i in range(1,l):
		Prix_Moyen.append(aHotelDB.prix_moyen_hotel(i))   #liste des prix moyens des nuits pour chaque hotel
		Nom_Hotel.append(aHotelDB.liste_nom_hotel()[i][0])#liste des noms des hotels
		Prix+=aHotelDB.prix_hotel(i)                      #construction de la liste de tous les prix des nuits dans tous les hotels


	AVG=sum(Prix)/len(Prix)
	plt.figure(figsize = (10, 10))
	plt.barh(range(1,l),Prix_Moyen,  edgecolor = ['blue' for i in range(1,l)],color = ['yellow' for i in range(1,l)],linestyle = 'solid', hatch ='/')
	plt.yticks(range(1,l), Nom_Hotel)
	plt.title("Prix moyen des chambres dans les hotels")

	plt.plot([AVG,AVG],[0,l],linestyle = 'dashed', linewidth = 2)#ligne verticale correspondant à la moyenne totale des prix
	plt.text(AVG, -0.3, "Moyenne",horizontalalignment = 'center', verticalalignment = 'center')

	plt.show()

def date_diff(l):#retourne la differrence de jours entre deux dates avec une liste de type [('AAAA-MM-JJ', 'AAAA-MM-JJ')]
	if type(l)!=list:
		print("Ce n'est pas une liste")
	else:
		arrivee=list(l[0][0]);depart=list(l[0][1])

		L_arrivee=[int(i) for i in [arrivee[0]+arrivee[1]+arrivee[2]+arrivee[3]]]+[int(i) for i in [arrivee[5]+arrivee[6]]]+[int(i) for i in [arrivee[8]+arrivee[9]]]
		L_depart=[int(i) for i in [depart[0]+depart[1]+depart[2]+depart[3]]]+[int(i) for i in [depart[5]+depart[6]]]+[int(i) for i in [depart[8]+depart[9]]]

		date_arrivee=date(L_arrivee[0],L_arrivee[1],L_arrivee[2])#type date de python
		date_depart=date(L_depart[0],L_depart[1],L_depart[2])

		return (date_depart-date_arrivee).days

def camenbert_duree_occupation():#affiche le camembert
	l=len(aHotelDB.liste_resa())
	L_nbjour=[]
	Labels=['1 jour','2 jours', '3 jours','4 jours', '5 à 10 jours','10 à 20 jours', 'Plus de 20 jours']#liste de classes de proportions
	L_compteur_labels=[0,0,0,0,0,0,0]#initialisation des compteurs
	for i in range(1,l):
		nbjour=date_diff(aHotelDB.dates(i))
		if nbjour==1:
			L_compteur_labels[0]+=1
		elif nbjour==2:
			L_compteur_labels[1]+=1
		elif nbjour==3 :
			L_compteur_labels[2]+=1
		elif nbjour==4:
			L_compteur_labels[3]+=1
		elif nbjour>4 and nbjour<=10:
			L_compteur_labels[4]+=1
		elif nbjour>10 and nbjour<=20:
			L_compteur_labels[5]+=1
		elif nbjour>20:
			L_compteur_labels[6]+=1

	plt.title("Durée d'occupation des clients")

	plt.pie(L_compteur_labels, labels = Labels,
			colors = ['red', 'green', 'yellow'],
			explode = [0, 0, 0, 0, 0,0, 0.1 ],#permet de faire sortir une part du camembert
			autopct = lambda x: str(round(x, 2)) + '%',#écriture des pourcentages
			pctdistance = 0.8, labeldistance = 1.1,#distance du texte par rapport au centre du camembert
			shadow = True)#affichage de l'ombre
	plt.show()
