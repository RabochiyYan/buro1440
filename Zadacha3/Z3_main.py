def pyatinachi(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return pyatinachi(n-1)*5 + pyatinachi(n-2)

def main(n):
    buf = [1,3]
    A = [1,3]
    i = 2
    while len(A) != n:
        p = buf[i-1]*5 + buf[i-2]
        i+=1
        buf.append(p)
        if p%2==1:
            A.append(p)

    return A[-1]


if __name__ == "__main__":
    import time
    start_time = time.time()

    print(main(int(input())))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.4f} секунд")