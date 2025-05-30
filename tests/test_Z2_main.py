from Zadacha2.Z2_main import main
from Zadacha2.Z2_main import input_v2


def test_input_v2():
    assert input_v2(0) == (5, [1, 10, 6, 7, 18], 'NONE')
    assert input_v2(3) == (28, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 21, 23, 25, 26, 1, 24, 1], 26)



def test_main():
    start = 0
    while True:
        print(start)
        n, otrs, ans = input_v2(start)
        if n == -1:
            break

        assert main(2, start) == ans
        start += 2+(n if n==0 else 1)
