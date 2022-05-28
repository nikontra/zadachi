import sys


def recursion_fibonacci(n, k):
    com_prev = 0
    com = 1
    cached = [com_prev, com]

    for curr in range(1, n):
        com_old = com
        com = (com_old + com_prev) % k
        com_prev = com_old

        if com_prev == 0 and com == 1:
            cached.pop()
            break
        else:
            cached.append(com)

    offset = n % len(cached)
    sys.stdout.write(str(cached[offset]))


def main():
    list_string = sys.stdin.readline().split(" ")
    n = list_string[0]
    k = list_string[1]
    f = recursion_fibonacci(n, k)

    print(f)


if __name__ == '__main__':
    main()
