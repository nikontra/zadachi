def read_input():
    num_line = int(input())
    num_column = int(input())
    matrix = []
    for i in range(num_line):
        matrix.append(list(map(int, input().strip().split())))
    return matrix, num_line, num_column


def queue_list(matrix, num_line, num_column):
    new_matrix = []
    for j in range(num_column):
        new_line = []
        for i in range(num_line):
            new_line.append(matrix[i][j])
        new_matrix.append(new_line)
        print(*new_line)
    return new_matrix


def main():
    matrix, num_line, num_column = read_input()
    queue_list(matrix, num_line, num_column)


if __name__ == "__main__":
    main()
