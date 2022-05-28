import sys
from functools import cmp_to_key


def less(object_1, object_2):
    return int(object_1 + object_2) < int(object_2 + object_1)


def sort_vial(arr, func_comparator):
    n = len(arr)
    while n > 1:
        f = 0
        for i in range(n-1):
            if func_comparator(arr[i], arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                f = 1
        n -= 1
        if f == 0:
            return arr
    return arr


def read_input():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    arr = line.split()
    return arr, n


def main():
    arr = read_input()
    # sort_arr = sort_vial(arr, less)
    result = sorted(arr, key=cmp_to_key(less))
    print(result)
    # print(''.join(sort_arr))


if __name__ == '__main__':
    main()
