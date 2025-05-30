def main():
    n, otrs = input_v2(0)

    otrs.sort()

    otrs = otrs[::-1]


    return otrs


def input_v1():
    n = int(input())
    otrs = []
    for _ in range(n):
        x = tuple(input().split())
        otrs.append(x)
    return n, otrs

def input_v2(start):
    with open('Zadacha1/input.txt', 'r') as file:
        lines = file.readlines()
    
    n = int(lines[start])
    otrs = list(map(lambda x: tuple(map(int, x.split())), lines[start+1:start+n+1]))


    return n, otrs


print(main())