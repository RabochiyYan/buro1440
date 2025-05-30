def input_v1():
    n = int(input())
    otrs = []
    for _ in range(n):
        x = tuple(input().split())
        otrs.append(x)
    return n, otrs

def input_v2(start):
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')

    with open(input_path, 'r') as file:
        lines = file.readlines()

    ans = int(lines[start])
    if ans == -1:
        return -1, -1, -1
    n = int(lines[start+1])
    otrs = list(map(lambda x: tuple(map(int, x.split())), lines[start+2:start+n+2]))

    return n, otrs, ans



def main(input_version, start):

    if input_version == 1:
        n, otrs = input_v1()
    else:
        n, otrs, _ = input_v2(start)

    if n == 0:
        return 0

    otrs.sort(key=lambda x: x[1])
    points = []
    x = otrs[0][1]
    points.append(x)

    for otr in otrs[1:]:
        l, r = otr
        if x < l:
            x = r
            points.append(x)

    return len(points)


if __name__ == "__main__":
    print(main(1,-1))
