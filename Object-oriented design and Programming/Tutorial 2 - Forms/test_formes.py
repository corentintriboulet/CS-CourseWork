##Test formes

from formes import *

def test_Rectangle():
    r = Rectangle((10, 20), (100, 50))
    str(r)
    #assert r.contient_point(50, 50) False
    assert not r.contient_point(0, 0)
    r.redimension_par_points(100, 200, 1100, 700)
    assert r.contient_point(500, 500)
    assert not r.contient_point(50, 50)

def test_Ellipse():
    e = Ellipse((60, 45), (50, 25))
    str(e)
    assert e.contient_point(50, 50)
    assert not e.contient_point(11, 21)
    e.redimension_par_points(100, 200, 1100, 700)
    assert e.contient_point(500, 500)
    assert not e.contient_point(101, 201)

def test_Cercle():
    c = Cercle((10, 20), 30)
    str(c)
    assert c.contient_point(0, 0)
    assert not c.contient_point(-19, -9)
    c.redimension_par_points(100, 200, 1100, 700)
    #assert c.contient_point(500, 500) false
    assert not c.contient_point(599, 500)

if __name__ == '__main__':
    test_Rectangle()
    test_Ellipse()
    test_Cercle()
