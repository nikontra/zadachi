a = int(input())
string = str(input())
list_int = list(map(int, string.split()))

def randomness(list_int):
    counter = 0

    if len(list_int) == 1:
        counter += 1
        return counter

    if list_int[0] > list_int[1]:
        counter += 1

    if list_int[-1] > list_int[-2]:
        counter += 1

    for i in range(1, (len(list_int)-1)):
        if list_int[i-1] < list_int[i] > list_int[i+1]:
            counter += 1
    return counter

print(randomness(list_int))