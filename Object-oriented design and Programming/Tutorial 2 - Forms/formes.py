import matplotlib.pyplot as plt
import numpy as np
##Formes

class Forme:
    def __init__(self,centre):
        self.__centre=centre
    def __str__(self):
        return print('Cette forme a pour centre ' + str(self.__centre))

    def get_centre(self):
        return  self.__centre

    def set_centre(self,c:tuple	):
        self.__centre=c

    def translation(self,dx, dy):
        set_centre(self,(self.__centre[0]+dx,self.__centre[1]+dy))

if __name__ == '__main__':
    pass

##Rectangle

class Rectangle(Forme):
    def __init__(self,centre,dim):
        Forme.__init__(self,centre)
        self.__dim=dim

    def __str__(self):
        S= 'Rectangle:'+'\n'+ '  Centre (x,y): '+ str(self.get_centre()) + '\n'+ '  Longueur et hauteur: '+ str(self.__dim)
        return S

    def get_dim(self):
        return self.__dim

    def set_dim(self,d):
        self.__dim=d

    def contient_point(self,x,y):
        x_bool=0;y_bool=0
        if (x>=(self.get_centre()[0]-self.__dim[0]/2)) and (x<=(self.get_centre()[0]+self.__dim[0]/2)):
            x_bool=1
        if (y>=(self.get_centre()[1]-self.get_centre()[1]/2)) and (y<=(self.get_centre()[1]+self.__dim[1]/2)):
            y_bool=1
        return (x_bool,y_bool)==(1,1)

    def redimension_par_points(self,x0, y0, x1, y1):
        self.set_centre(((x0+x1)/2,(y0+y1)/2))
        self.set_dim((abs(x0-x1),abs(y0-y1)))
##Ellispe

class Ellipse(Forme):
    def __init__(self,centre,rayons):
        Forme.__init__(self,centre)
        self.__rayons=rayons
    def __str__(self):
        S='Elispe: '   + '\n'+'  Centre:'    + str(self.get_centre()) + '\n'+ '  Rx et Ry: ' + str(self.__rayons)
        return S

    def set_rayons(self,r):
        self.__rayons=r

    def get_rayons(self):
        return self.__rayons

    def contient_point(self,x,y):
        return ((x-self.get_centre()[0])**2/(self.__rayons[0])**2 + (y-self.get_centre()[1])**2/(self.__rayons[1])**2)<=1

    def redimension_par_points(self,x0, y0, x1, y1):
        self.set_centre(((x0+x1)/2,(y0+y1)/2))
        self.set_rayons((abs(x0-x1)/2,abs(y0-y1)/2))

##Cercle
def sg(a,b):        #fonction signe
        if a-b<0:
            return -1
        else:
            return 1

class Cercle(Ellipse):
    def __init__(self,centre,rayon):
        Ellipse.__init__(self,centre,(rayon,rayon))

    def __str__(self):
        S='Cercle: '  +'\n'+ '  Centre:' + str(self.get_centre()) + '\n'+ '  Rayon: ' + str(self.get_rayons()[0])
        return S



    def redimension_par_points(self,x0, y0, x1, y1):
        r=min(abs(x0-x1),abs(y0-y1))
        xc=x0+sg(x0,x1)*r
        yc=y0+sg(y1,y0)*r
        self.set_centre((xc,yc))
        self.set_rayons((r,r))

R1 = Rectangle((10, 20), (100, 50))
R2 = Rectangle((0, 0), (2, 2))
E1 = Ellipse((0,0),(1,2))
C1 = Cercle((0,0),1)
##Matplotlib


def affiche_rectangle(centre,dim):
    xc,yc=centre
    H,L=dim
    h=H/2;l=L/2
    Lx=[xc-h,xc+h,xc+h,xc-h,xc-h]
    Ly=[yc+l,yc+l,yc-l,yc-l,yc+l]
    plt.plot(Lx,Ly)

def affiche_point(x,y):
    plt.plot(x,y,"+")
def affiche_rectangle2(x0,y0,x1,y1):
    plt.plot([x0,x1,x1,x0,x0],[y0,y0,y1,y1,y0])
def affiche_ellipse(centre,rayons):
    xc,yc=centre;rx,ry=rayons
    Lx=np.linspace(xc-rx,xc+rx,100)
    Ly_plus=equa_ellipse_plus(Lx,xc,yc,rx,ry)
    Ly_moins=equa_ellipse_moins(Lx,xc,yc,rx,ry)
    plt.plot(Lx,Ly_plus)
    plt.plot(Lx,Ly_moins)
    plt.plot(xc,yc,"o")

def equa_ellipse_plus(X,xc,yc,rx,ry):
    return yc + ry*np.sqrt(1-((X-xc)/rx)**2)

def equa_ellipse_moins(X,xc,yc,rx,ry):
    return yc - ry*np.sqrt(1-((X-xc)/rx)**2)
def affiche_ellipse2(x0,y0,x1,y1):
    return affiche_ellipse(((x0+x1)/2,(y0+y1)/2),(abs(x0-x1)/2,abs(y0-y1)/2))
##Programme test
def test_rect():
    affiche_rectangle((10, 20), (100, 50))
    affiche_point(50,50)
    affiche_rectangle2(100, 200, 1100, 700)
    affiche_point(500, 500)

    affiche_point(0,0)
    plt.axis()
    plt.grid()
    plt.show()

def test_elli():
    affiche_ellipse((60, 45), (50, 25))
    affiche_point(50, 50)
    affiche_point(11, 21)
    affiche_ellipse2(100, 200, 1100, 700)
    affiche_point(500, 500)
    affiche_point(101, 201)


    affiche_point(0,0)
    plt.axis()
    plt.grid()
    plt.show()


