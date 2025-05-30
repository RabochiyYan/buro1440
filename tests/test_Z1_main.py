from Zadacha1.Z1_main import main
from Zadacha1.Z1_main import min_points_to_cover_segments2
from Zadacha1.Z1_main import input_v2
import sys
from io import StringIO


def test_input_v2():
    assert input_v2(0) == (5, [(1,2), (2,4), (4,5), (5,6), (4,7)], 2)
    assert input_v2(7) == (7, [(0,5),(2,8),(4,9),(6,11),(10,12),(11,14),(10,15)], 2)
    assert input_v2(16) == (4, [(1,4), (3,5), (4,8), (11,15)], 2)



def test_main():
    start = 0
    while True:
        print(start)
        n, otrs, ans = input_v2(start)
        if n == -1:
            break

        assert min_points_to_cover_segments2(2, start) == ans
        start += 2+n


