def dec_bin(num_dec):
    num_bin = ''
    while num_dec>=2:
        num_bin += str(num_dec%2)
        num_dec = num_dec//2
    num_bin += str(num_dec)

    return num_bin[::-1]


def main():
    num_dec = int(input())
    print(dec_bin(num_dec))


if __name__ == "__main__":
    main()
