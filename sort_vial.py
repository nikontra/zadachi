import sys


def sort_vial(arr):
    n = len(arr)
    while n > 1:
        f = 0
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                f = 1
        if f == 0:
            if n == len(arr):
                print(*arr)
            break
        n -= 1
        print(*arr)


def read_input():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    arr = list(map(int, line.split()))
    return arr, n

# def read_input():
#     with open('input.txt', 'r') as f:
#         n = f.readline().rstrip()
#         line = f.readline().rstrip()
#         f.close()
#     arr = list(map(int, line.split()))
#     return arr, n


def main():
    arr, n = read_input()
    sort_vial(arr)


if __name__ == '__main__':
    main()
