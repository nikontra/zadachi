def bracket(n, prefix='', left_bracket=0, right_bracket=0):
    if left_bracket == n and right_bracket == n:
        print(prefix)
    else:
        if left_bracket < n:
            bracket(n, prefix + '(', left_bracket+1, right_bracket)
        if right_bracket < left_bracket:
            bracket(n, prefix + ')', left_bracket, right_bracket+1)


def main():
    n = int(input())
    bracket(n)


if __name__ == '__main__':
    main()
