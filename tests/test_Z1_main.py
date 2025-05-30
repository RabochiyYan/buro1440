from Zadacha1.Z1_main import main
from Zadacha1.Z1_main import input_v2
import sys
from io import StringIO


def test_input_v2():
    assert input_v2(0) == (5, [(1,2), (2,4), (4,5), (4,6), (4,7)])