import sys


def sort_line(arr):
    counted_value = [0] * 3
    for value in arr:
        counted_value[value] += 1

    index = 0
    for value in range(0, 3):
        for amount in range(0, counted_value[value]):
            arr[index] = value
            index += 1


def read_input():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    wardrobe = list(map(int, line.split()))
    return wardrobe, n


def main():
    wardrobe, n = read_input()
    sort_line(wardrobe)
    print(*wardrobe)


if __name__ == '__main__':
    main()
