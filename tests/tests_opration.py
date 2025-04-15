# importing func from src file so we can check test case
from src.math_oparation import add, sub

def test_add(a,b):
    assert add(2,3)==5 # assert check o/p
    assert add(-1,1)==0
   
def test_sub(a,b):
     assert (-1,1)==-2
     assert (1,1)==0
     assert (4,1)==3