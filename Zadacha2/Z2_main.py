def input_v2(start):
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')

    with open(input_path, 'r') as file:
        lines = file.readlines()

    ans = lines[start]
    if ans == '-1':
        return -1, -1, -1
    elif ans == 'NONE\n':
        ans = 'NONE'
    else:
        ans = int(ans)

    n = int(lines[start+1])
    if n!=0:
        letters = list(map(int, lines[start+2].split()))
    else:
        letters = []

    return n, letters, ans

def input_v1():
    n = int(input())
    letters = list(map(int, input().split()))
    return n, letters

def main(input_version, start):

    if input_version == 1:
        n, letters = input_v1()
    else:
        n, letters, _ = input_v2(start)

    """
    if n < 26:
        return 'NONE'
    """

    ideal=[]
    for i in range(1,27):
        ideal.append(i)
    ideal = set(ideal)

    buf = []
    best = n+1

    for i in range(len(letters)-25):
        for letter in letters[i:]:
            buf.append(letter)
            if ideal.issubset(set(buf)):
                if len(buf) < best:
                    best = len(buf)
                buf = []
                break
    return 'NONE' if best==n+1 else best


if __name__ == "__main__":
    print(main(1, -2))