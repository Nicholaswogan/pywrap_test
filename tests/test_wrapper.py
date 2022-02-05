import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from pywrap_test import pywrap_test as t
import numpy as np

def test_scalars():
    t.i1 = 1
    assert t.i1 == 1
    
    assert t.i2 == 3
    
    t.i3 = 3
    assert t.i3 == 3
    
    t.r1 = 1.0
    assert t.r1 == 1.0
    
    t.l1 = False
    assert t.l1 == False
    
    t.c1 = 1j + 10
    assert t.c1 == 1j + 10
    
def test_arrays():
    arr1_ = np.ones((8,),np.float32)*0.1
    t.arr1 = arr1_
    assert np.all(t.arr1 == arr1_)
    
    assert np.all(t.arr2 == np.array([1,2,3],np.float32))
    
    arr3_ = np.ones((100,),np.float32)*0.1
    t.arr3 = arr3_
    assert np.all(t.arr3 == arr3_)
    
    arr4_ = np.ones((10,11),np.bool_)
    t.arr4 = arr4_
    assert np.all(t.arr4 == arr4_)
    
    arr5_ = np.ones((3,),np.int32)*2
    t.arr5 = arr5_
    assert np.all(t.arr5 == arr5_)
    
def test_derivedtypes():
    m = t.mytype()
    m.i = 10
    assert m.i == 10
    
    arr_ = np.array([1,2,3,4,5],np.float32)
    m.arr = arr_
    assert np.all(m.arr == arr_)
    

