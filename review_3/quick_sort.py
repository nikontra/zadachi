#  ID: 68764915
import sys


def partition(arr: list, left: int, right: int) -> int:
    """Возвращает опорный элемент."""
    i: int = (left - 1)
    pivot: int = arr[right]
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return (i + 1)


def quick_sort(arr: list, left: int, right: int) -> list:
    """Рекурсивно сортирует полученый список."""
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
        return arr


def read_input() -> list:
    """Принимает и обрабатывает вводные данные."""
    arrs: list = []
    for i in range(int(sys.stdin.readline())):
        line: str = sys.stdin.readline()
        arr: list = line.split()
        arr[0], arr[2] = arr[2], arr[0]
        arr[0], arr[1] = -int(arr[1]), int(arr[0])
        arrs.append(arr)
    return arrs


def main() -> None:
    arrs: list = read_input()
    sort_arrs = quick_sort(arrs, 0, len(arrs)-1)
    for arr in sort_arrs:
        print(arr[2])


if __name__ == '__main__':
    main()
