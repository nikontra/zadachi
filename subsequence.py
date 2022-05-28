def read_input():
    s = input()
    t = input()
    return s, t


def main():
    s, t = read_input()
    result = True
    if s == '' or t == '':
        result = False
    for i in s:
        if i not in t:
            result = False
            break
    print(result)


if __name__ == '__main__':
    main()
