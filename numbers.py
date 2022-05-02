import sys

def even_odd_num(numbers):
    even_list = []
    odd_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    if len(even_list) == 3 or len(odd_list) == 3:
        return "WIN"
    return "FAIL"

def main():
    line = sys.stdin.readline().rstrip()
    line_list = line.split()
    numbers = list(map(int, line_list))
    numbers_three = numbers[:3]
    print(even_odd_num(numbers_three))

if __name__ == '__main__':
    main()
