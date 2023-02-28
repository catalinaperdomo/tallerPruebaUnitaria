from funcion import numero_menor

def test_numero_menor():
    assert numero_menor([5,3,9,20,45])==3
    assert numero_menor([15,2,25,10,51])==2
    assert numero_menor([1,4,3,16,5])==1
    assert numero_menor([20,13,19,22,15])==13