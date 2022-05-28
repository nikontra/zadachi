import sys


def search_day(arr, s, left, right):
    if right <= left:
        return -1

    mid = (left + right) // 2
    if arr[mid] >= s and mid == 0:
        return mid + 1
    elif arr[mid] >= s and arr[mid - 1] < s:
        return mid + 1
    elif arr[mid] < s:
        return search_day(arr, s, (mid + 1), right)
    else:
        return search_day(arr, s, left, mid)


def read_input():
    l = int(input())
    line_day = sys.stdin.readline().rstrip()
    days = list(map(int, line_day.split()))
    s = int(input())
    return days, s


def main():
    days, s = read_input()
    x_1 = search_day(days, s, left=0, right=len(days))
    x_2 = search_day(days, s*2, left=0, right=len(days))
    y = [x_1, x_2]
    print(*y)


if __name__ == "__main__":
    main()
