def recursion_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursion_fibonacci(n-1)+recursion_fibonacci(n-2)


def main():
    n = int(input())
    print(recursion_fibonacci(n))


if __name__ == '__main__':
    main()
