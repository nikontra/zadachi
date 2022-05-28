# with open('input.txt', 'r') as f:
#     lines = f.readlines()
#     num_lines = int(lines.pop(0))
#     num_collomns = int(lines.pop(0))
#     index_collomn = int(lines.pop(-1))
#     index_line = int(lines.pop(-1))

# matrix = []

# for line in lines:
#     list_int = list(map(int, line.split()))
#     matrix.append(list_int)

# def get_neighbors(a, b):
#     d = {(i, c):matrix[i][c] for i in range(len(matrix)) for c in range(len(matrix[0]))}
#     return filter(None, [d.get(i) for i in [(a-1, b), (a, b+1), (a+1, b), (a, b-1)]])

# list_neighbors = get_neighbors(index_line, index_collomn)
# list_int = list(list_neighbors)
# list_int.sort()

# print(' '.join(list(map(str, list_int))))
# from typing import List, Tuple


# def read_input():
#     num_lines = int(input())
#     num_collomns = int(input())
#     matrix = []
#     for i in range(num_lines):
#         matrix.append(list(map(int, input().strip().split())))
#     index_line = int(input())
#     index_colomn = int(input())
#     return matrix, num_lines, num_collomns, index_line, index_colomn

with open('input.txt', 'r') as f:
    lines = f.readlines()
    num_lines = int(lines.pop(0))
    num_collomns = int(lines.pop(0))
    index_collomn = int(lines.pop(-1))
    index_line = int(lines.pop(-1))

matrix = []

for line in lines:
    list_int = list(map(int, line.split()))
    matrix.append(list_int)


def neighbors_left(matrix, index_line, index_collomn):
    if index_collomn == 0:
        return None
    return matrix[index_line][(index_collomn-1)]


def neighbors_right(matrix, index_line, num_collomns, index_collomn):
    if (index_collomn+1) == num_collomns:
        return None
    return matrix[index_line][(index_collomn+1)]


def neighbors_top(matrix, index_line, index_collomn):
    if index_line == 0:
        return None
    return matrix[(index_line-1)][index_collomn]


def neighbors_bottom(matrix, index_line, num_lines, index_collomn):
    if (index_line+1) == num_lines:
        return None
    return matrix[(index_line+1)][index_collomn]


def search_neighbors(matrix, index_line, num_collomns, index_collomn, num_lines):
    list_neighbors = []

    top = neighbors_top(matrix, index_line, index_collomn)
    if top is not None:
        list_neighbors.append(top)

    bottom = neighbors_bottom(matrix, index_line, num_lines, index_collomn)
    if bottom is not None:
        list_neighbors.append(bottom)

    left = neighbors_left(matrix, index_line, index_collomn)
    if left is not None:
        list_neighbors.append(left)

    right = neighbors_right(matrix, index_line, num_collomns, index_collomn)
    if right is not None:
        list_neighbors.append(right)

    list_neighbors.sort()

    list_str = list(map(str, list_neighbors))

    string_neighbors = ' '.join(list_str)

    return string_neighbors


print(search_neighbors(matrix, index_line, num_collomns, index_collomn, num_lines))
