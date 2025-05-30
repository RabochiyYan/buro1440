from Zadacha3.Z3_main import pyatinachi
from Zadacha3.Z3_main import main


def test_pyatinachi():
    anses = [1,3,16,83,431,2238,11621,60343]

    for i in range(len(anses)):
        assert pyatinachi(i) == anses[i]


def test_main():
    assert main(6) == 60343