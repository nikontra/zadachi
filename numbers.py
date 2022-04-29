string = str(input())
list_str = string.split()
numbers = list(map(int, list_str))

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

print(even_odd_num(numbers))
