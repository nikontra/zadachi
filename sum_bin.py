def sum_num(num_1, num_2):
    len_num_1 = len(num_1)
    len_num_2 = len(num_2)
    if len_num_1 == len_num_2 or len_num_1 > len_num_2:
        max_num = num_1
        min_num = num_2
    else:
        max_num = num_2
        min_num = num_1
    dif_len_num = abs(len_num_1 - len_num_2)

    max_len = max(len(num_1), len(num_2))
    num_1_rev = max_num[::-1]
    num_2_rev = min_num[::-1]
    num_2_rev += '0' * dif_len_num
    num_rev = ''
    digit = 0
    for i in range(max_len):
        sum = int(num_1_rev[i]) + int(num_2_rev[i])
        if digit == 0:
            if sum < 2:
                num_rev += str(sum)
            else:
                num_rev += '0'
                digit = 1
        else:
            if sum == 0:
                num_rev += str(digit)
                digit = 0
            elif sum == 1:
                num_rev += '0'
                digit = 1
            else:
                num_rev += str(digit)
                digit = 1

    if digit > 0:
        num_rev += str(digit)
    return num_rev[::-1]


def read_input():
    """Принимает и обрабатывает вводные данные."""
    num_bin_1 = str(input())
    num_bin_2 = str(input())
    return num_bin_1, num_bin_2


def main():
    num_1, num_2 = read_input()
    result = sum_num(num_1, num_2)
    print(result)


if __name__ == "__main__":
    main()
