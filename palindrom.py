import sys

def palindrom(line):
    line_filter = ''.join(
        simbol for simbol in line if simbol.isalnum()
    ).lower()
    if line_filter == line_filter[::-1]:
        return True
    return False

def main():
    line = sys.stdin.readline().rstrip()
    print(palindrom(line))

if __name__ == "__main__":
    main()