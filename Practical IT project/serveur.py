import http.server
import socketserver
import sqlite3
import json
import datetime
import ast

from urllib.parse import urlparse, parse_qs, unquote


#
# Définition du nouveau handler
#
class RequestHandler(http.server.SimpleHTTPRequestHandler):

  # sous-répertoire racine des documents statiques
  static_dir = '/client'


  #
  # On surcharge la méthode qui traite les requêtes GET
  #
  def do_GET(self):
    # on récupère les paramètres
    self.init_params()

    # le chemin d'accès commence par /time
    if self.path.startswith('/time'):
      self.send_time()

    # s'il y a l'erreur favicon
    elif len(self.path_info) > 0 and self.path_info[0] == 'favicon.ico':
      self.send_error(204)

    # le chemin d'accès commence par le nom de projet au pluriel
    elif len(self.path_info) > 1 and self.path_info[0] == "description":
      self.send_json_volcan(self.path_info[1])

    # le chemin d'accès commence par le nom du projet au singulier, suivi par un nom de lieu
    elif len(self.path_info) > 0 and self.path_info[0] == "location":
      self.send_json_volcans()


    elif len(self.path_info) > 0 and self.path_info[0] == "commentaires":
        self.get_commentaire()

    # ou pas...
    else:
      self.send_static()

  #
  # On surcharge la méthode qui traite les requêtes HEAD
  #
  def do_HEAD(self):
    self.send_static()

  # On surcharge la méthode qui traite les requêtes POST
  #
  def do_POST(self):
    self.init_params()

    if len(self.path_info) > 0 and self.path_info[0] == "commentaire":
        self.POST_commentaire()

    elif len(self.path_info) >0 and self.path_info[0]== "utilisateur":
      self.POST_utilisateur()

    else:
        self.send_static()


  #On surcharge la méthode qui traite les requêtes DELETE
  def do_DELETE(self):
    self.init_params()

    if len(self.path_info) > 0 and self.path_info[0] == "commentaire":
        self.delete_commentaire()
    else:
        self.send_static()


  #Création d'un commentaire
  def POST_commentaire(self):
      dic = ast.literal_eval(self.body)
      if dic["pseudo"] == "" or dic["password"] == "" or dic["date"] == "" or dic["message"] == "" :
          self.send_error(422, "Il manque des informations")
      else:
          c = conn.cursor()

          c.execute("SELECT mdp FROM utilisateurs WHERE pseudo = '" + dic["pseudo"] + "'")
          test = False
          utilisateurs = c.fetchall()
          for utilisateur in utilisateurs:
              if utilisateur[0] == dic["password"]:
                  test = True
          if test:
              date = datetime.datetime.today().ctime()
              print(date)
              c.execute("SELECT COUNT(*) FROM commentaires")
              count = c.fetchone()[0]
              inser = "INSERT INTO commentaires VALUES ("
              inser += "'"+str(count)+"',"
              inser += "'"+dic["pseudo"]+"',"
              inser += "'"+dic["site"]+"',"
              inser += "'"+date+"',"
              inser += "'"+dic["message"]+"',"
              inser += "'"+dic["date"]+"')"
              c = c.execute(inser)
              conn.commit()
              dic["timestamp"] = date
              self.send_json(dic)
          else :
              self.send_error(401,"Le mot de passe ou le pseudo sont incorrects")



  #Création d'un utilisateur
  def POST_utilisateur(self):
      dic = ast.literal_eval(self.body)
      if dic["user_pseudo"] == "" or dic["email"] == "" or dic["user_password"] == "" :
          self.send_error(422, "Il manque des informations")
      else:
          c = conn.cursor()
          c.execute("SELECT pseudo FROM utilisateurs")
          test = True
          utilisateurs = c.fetchall()
          for utilisateur in utilisateurs:
              if utilisateur[0] == dic["user_pseudo"]:
                  test = False
          if test:
              inser = "INSERT INTO utilisateurs VALUES ("
              inser += "'"+dic["user_pseudo"]+"',"
              inser += "'"+dic["email"]+"',"
              inser += "'"+dic["user_password"]+"')"
              c = c.execute(inser)
              conn.commit()
              self.send_json(dic)
          else:
            self.send_error(409, "Le pseudo existe déjà")





  #Récupération de la liste des commentaires sur un site
  def get_commentaire(self):
    L = []
    c = conn.cursor()
    c.execute("SELECT * FROM commentaires WHERE volcan= '" + self.path_info[1]+"'")
    data = c.fetchall()
    for d in data:
        dic = {"id":d[0],
               "pseudo": d[1],
               "site":d[2],
               "message":d[4],
               "date":d[5],
               "timestamp":d[3]}
        L.append(dic)
    self.send_json(L)

  #Suppression d'un commentaire
  def delete_commentaire(self):
    dic = ast.literal_eval(self.body)
    c = conn.cursor()
    c.execute("SELECT * FROM utilisateurs WHERE pseudo = '" + dic["pseudo"]+"'")
    utilisateurs = c.fetchall()

    test = False

    for utilisateur in utilisateurs:
        if dic["password"] == utilisateur[2]:
            test = True

    if test:
        c.execute("DELETE FROM commentaires WHERE id= '" + self.path_info[1]+"'")
        conn.commit()
        self.send_response(204)
        self.send_json(dic)
    else:
      self.send_error(410, "Le mot de passe est incorrect")



  # On envoie le document statique demandé
  #
  def send_static(self):

    # on modifie le chemin d'accès en insérant un répertoire préfixe
    self.path = self.static_dir + self.path

    # on appelle la méthode parent (do_GET ou do_HEAD)
    # à partir du verbe HTTP (GET ou HEAD)
    if (self.command=='HEAD'):
        http.server.SimpleHTTPRequestHandler.do_HEAD(self)
    else:
        http.server.SimpleHTTPRequestHandler.do_GET(self)


  # On envoie un document au format json
  #
  def send_json(self,data):
    headers = [('Content-Type','application/json')]
    self.send(json.dumps(data),headers)


  #
  # on analyse la requête pour initialiser nos paramètres
  #
  def init_params(self):
    # analyse de l'adresse
    info = urlparse(self.path)
    self.path_info = [unquote(v) for v in info.path.split('/')[1:]]  # info.path.split('/')[1:]
    self.query_string = info.query
    self.params = parse_qs(info.query)

    # récupération du corps
    length = self.headers.get('Content-Length')
    ctype = self.headers.get('Content-Type')
    if length:
      self.body = str(self.rfile.read(int(length)),'utf-8')
      if ctype == 'application/x-www-form-urlencoded' :
        self.params = parse_qs(self.body)
    else:
      self.body = ''

    # traces
    print('path_info =',self.path_info)
    print('body =',length,ctype,self.body)
    print('params =', self.params)


  #
  # On envoie un document avec l'heure
  #
  def send_time(self):

    # on récupère l'heure
    time = self.date_time_string()

    # on génère un document au format html
    body = '<!doctype html>' + \
           '<meta charset="utf-8">' + \
           '<title>l\'heure</title>' + \
           '<div>Voici l\'heure du serveur :</div>' + \
           '<pre>{}</pre>'.format(time)

    # pour prévenir qu'il s'agit d'une ressource au format html
    headers = [('Content-Type','text/html;charset=utf-8')]

    # on envoie
    self.send(body,headers)

  #
  # On renvoie la liste des volcans avec leurs coordonnées
  #
  def send_json_volcans(self):

    # on récupère la liste de volcans depuis la base de données
    r = self.db_get_volcans()
    # on renvoie une liste de dictionnaires au format JSON
    data = [{"name":d[0],"lat":d[1], "lon":d[2], "id":d[0]} for d in r]
    self.send_json(data)






  #
  # On renvoie les informations d'un volcan au format json
  #
  def send_json_volcan(self,volcans):

    # on récupère le volcan depuis la base de données
    r = self.db_get_volcan(volcans)

    # on n'a pas trouvé le volcan demandé
    if r == None:
      self.send_error(404,"Le Volcan n'a pas été trouvé")

    # on renvoie un dictionnaire au format JSON
    else:
        data = {"dbpedia":r[0],
               "name":r[1],
               "wiki":r[2],
               "desc":r[8],
               "photo":r[9],
               "eruption_date":r[6],
               "eruption_year":r[7],
               "elevation":r[3],
               "lat":r[4],
               "lon":r[5]}

        self.send_json(data)


  #
  # Récupération de la liste des volcan depuis la base
  #
  def db_get_volcans(self):
    c = conn.cursor()
    sql = 'SELECT name,lat,lon FROM volcans'

    # tous les volcans de la base
    c.execute(sql)
    return c.fetchall()



  #
  # Récupération d'un volcans dans la base
  #
  def db_get_volcan(self,volcans):
    # préparation de la requête SQL
    c = conn.cursor()
    # récupération de l'information (ou pas)
    c.execute("SELECT * FROM {} WHERE name=?".format(entity_list_name),(volcans,))
    r= c.fetchone()
    # construction de la réponse
    if r == None:
      self.send_error(404,"Le volcan {} n'a pas été trouvé".format(volcans))
    else :
      return r

  #
  # On envoie les entêtes et le corps fourni
  #
  def send(self,body,headers=[]):

    # on encode la chaine de caractères à envoyer
    encoded = bytes(body, 'UTF-8')

    self.send_response(200)

    [self.send_header(*t) for t in headers]
    self.send_header('Content-Length',int(len(encoded)))
    self.end_headers()

    self.wfile.write(encoded)



# nom dese entités traitées par votre projet, au pluriel
entity_list_name = "volcans"


# on en déduit le nom des entités au singulier
entity_name = entity_list_name[:-1]

#
# Ouverture d'une connexion avec la base de données
dbname = '{}.db'.format(entity_list_name)
conn = sqlite3.connect(dbname)

# Pour accéder au résultat des requêtes sous forme d'un dictionnaire
conn.row_factory = sqlite3.Row

#
# Instanciation et lancement du serveur
#
httpd = socketserver.TCPServer(("", 8080), RequestHandler)
httpd.serve_forever()

