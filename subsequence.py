def main():
    result = True
    s = input()
    t = input()
    start = -1
    for i in s:
        start = t.find(i, start + 1)
        if start == -1:
            result = False
    print(result)


if __name__ == '__main__':
    main()
