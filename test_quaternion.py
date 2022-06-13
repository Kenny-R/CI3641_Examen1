import quaternion as q

def test_suma():
    assert q.quaternion(1,2,3,4) + q.quaternion(1,2,3,4) == q.quaternion(2,4,6,8)
    assert q.quaternion(1)+2 == q.quaternion(3)
    assert q.quaternion(1,2,3,4) + ~q.quaternion(1,2,3,4) == q.quaternion(2)

def test_producto():
    assert (q.quaternion(1,2,3,4) * q.quaternion(1,2,3,4)) == q.quaternion(-28,4,6,8)
    assert q.quaternion(2.3,4.5)*2 == q.quaternion(2.3*2,4.5)
    assert (q.quaternion(1,2,3,4)*q.quaternion(-28,4,6,8) + q.quaternion(23,13,16)) == q.quaternion(-63,-39,-62,-104.0)

def test_inverso():
    assert ~q.quaternion(1,2,3,4) == q.quaternion(1,-2,-3,-4)
    assert ~q.quaternion() == q.quaternion()
    assert ~q.quaternion(1) == q.quaternion(1)
    assert ~q.quaternion(b = 2) == q.quaternion(b =-2)

def test_media():
    assert round(-q.quaternion(1,2,3,4),2)  == 5.48

def test_string():
    assert str(q.quaternion(1,2,3,4)) == "1+2i+3j+4k"


test_suma()
test_producto()
test_inverso()
test_media()
test_string()