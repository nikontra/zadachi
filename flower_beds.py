import sys


# def sort_items(item_1, item_2):
#     item_3 = []
#     sort_list = []
#     sort_list.append(item_1)
#     sort_list.append(item_2)
#     sort_list.sort()
#     if sort_list[0][1] < sort_list[1][0]:
#         item_3 = sort_list[0]
#     elif (sort_list[0] == sort_list[1]
#             or sort_list[0][0] == sort_list[1][0]):
#         item_3 = sort_list[1]
#     elif (sort_list[0][1] == sort_list[1][1]
#             or sort_list[0][1] > sort_list[1][1]):
#         item_3 = sort_list[0]
#     else:
#         item_3.append(sort_list[0][0])
#         item_3.append(sort_list[1][1])
#     return item_3
#         print(sort_list)


# def merge_sort(array):
#     if len(array) == 1:
#         return array

#     left = merge_sort(array[:(len(array)//2)])
#     right = merge_sort(array[(len(array)//2):len(array)])
#     result = []
#     k = 0
#     while len(left) != 0 or len(right) != 0:
#         sort_list = [left[0], right[0]]
#         sort_list.sort()
#         if sort_list[0][1] < sort_list[1][0]:
#             if sort_list[0] == left[0]:
#                 result[k] = left.pop(0)
#             else:
#                 result[k] = right.pop(0)
#         elif (sort_list[0] == sort_list[1]
#                 or sort_list[0][0] == sort_list[1][0]):
#             if sort_list[1] == left[0]:
#                 result[k] = left.pop(0)
#                 right.pop(0)
#             else:
#                 result[k] = right.pop(0)
#                 left.pop(0)
#         elif (sort_list[0][1] == sort_list[1][1]
#                 or sort_list[0][1] > sort_list[1][1]):
#             if sort_list[1] == left[0]:
#                 result[k] = left.pop(0)
#                 right.pop(0)
#             else:
#                 result[k] = right.pop(0)
#                 left.pop(0)
#             result[k] = [sort_list[0][0], sort_list[1][1]]
#             left.pop(0)
#             right.pop(0)
#         k += 1
#     if right is not None:
#         result[k] = right.pop(0)


def merge_sort(array):
    if len(array) == 1:
        return array

    left = merge_sort(array[:(len(array)//2)])
    right = merge_sort(array[(len(array)//2):len(array)])
    result = []
    while left and right:
        sort_list = [left[0], right[0]]
        sort_list.sort()
        if sort_list[0][1] < sort_list[1][0]:
            if sort_list[0] == left[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif (sort_list[0] == sort_list[1]
                or sort_list[0][0] == sort_list[1][0]):
            if sort_list[1] == left[0]:
                result.append(left.pop(0))
                right.pop(0)
            else:
                result.append(right.pop(0))
                left.pop(0)
        elif (sort_list[0][1] == sort_list[1][1]
                or sort_list[0][1] > sort_list[1][1]):
            if sort_list[1] == left[0]:
                result.append(left.pop(0))
                right.pop(0)
            else:
                result.append(right.pop(0))
                left.pop(0)
        else:
            result.append([sort_list[0][0], sort_list[1][1]])
            left.pop(0)
            right.pop(0)
        print(result)
    if right:
        result.append(right.pop(0))


def read_input():
    n = int(input())
    arrs = []
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        arr = line.split()
        arrs.append(arr)
    return arrs


def main():
    arrs = read_input()
    result = merge_sort(arrs)
    print(result)
    # for arr in result:
    #     print(*arr)


if __name__ == '__main__':
    main()
