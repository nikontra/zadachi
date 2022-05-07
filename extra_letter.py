def read_input():
    """Принимает и обрабатывает вводные данные."""
    line_1 = str(input())
    line_2 = str(input())
    return line_1, line_2


def extra_letter(line_1, line_2):
    list_2 = []
    for i in line_2:
        list_2.append(i)
    for i in line_1:
        list_2.remove(i)
    return list_2


def main():
    line_1, line_2 = read_input()
    result = extra_letter(line_1, line_2)
    print(*result)


if __name__ == "__main__":
    main()
