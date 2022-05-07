def sum_num(num):
    result = 0
    i = 0
    while result <= 10000:
        result = 4**i
        if 10000 >= result != num:
            i += 1
        elif result > 10000:
            return False
        else:
            return True


def read_input():
    """Принимает и обрабатывает вводные данные."""
    return int(input())


def main():
    num = read_input()
    result = sum_num(num)
    print(result)


if __name__ == "__main__":
    main()
