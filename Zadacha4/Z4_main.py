def f(n):
    n = str(n)
    n = n[::-1]
    buf = n
    for i in range(len(n)):
        if n[i] != '0':
            break
    return int(n[i:])

def g(n):
    return f(f(n))/n

def main(n):
    uniques = set()

    for i in range(1,n+1):
        uniques.add(g(i))

    return len(uniques)



if __name__ == "__main__":
    print(main(10**6))