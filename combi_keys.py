import sys

KEYS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combi_keys(line):
    ans = []
    if len(line) == 0:
        return []
    elif len(line) == 1:
        return KEYS[line]
    result = combi_keys(line[1:])
    for i in KEYS[line[0]]:
        for j in result:
            ans.append(i+j)
    return ans


def read_input():
    return sys.stdin.readline().rstrip()


def main():
    line = read_input()
    arr = combi_keys(line)
    print(*arr)


if __name__ == '__main__':
    main()
