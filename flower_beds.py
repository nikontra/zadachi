import sys


# def merge_sort(array):
#     if len(array) <= 1:
#         return array
#     midle = len(array)//2
#     left = merge_sort(array[:midle])
#     right = merge_sort(array[midle:len(array)])
#     result = [0] * len(array)
#     n = k = r = 0

#     while n < len(left) and r < len(right):
#         if left[n] <= right[r]:
#             result[k] = left[n]
#             n += 1
#         else:
#             result[k] = right[r]
#             r += 1
#         k += 1

#     while n < len(left):
#         result[k] = left[n]
#         n += 1
#         k += 1

#     while r < len(right):
#         result[k] = right[r]
#         r += 1
#         k += 1
#     return result


def change_array(array):
    result = []
    result.append(array[0])
    for i in range(1, len(array)):
        item_1 = result[-1]
        item_2 = array[i]
        if item_1[1] < item_2[0]:
            result.append(array[i])
        else:
            result[-1] = [min(item_1[0], item_2[0]), max(item_1[1], item_2[1])]
    return result


def read_input():
    arrs = []
    for i in range(int(sys.stdin.readline())):
        line = sys.stdin.readline()
        arr = list(map(int, line.split()))
        arrs.append(arr)
    return arrs


def main():
    arrs = read_input()
    result = sorted(arrs)
    for arr in change_array(result):
        print(*arr)


if __name__ == '__main__':
    main()
