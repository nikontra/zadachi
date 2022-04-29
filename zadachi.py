string = str(input())
n = int(input())
list_str = string.split()
lst = list(map(int, list_str))
lst_z = []

for i in range(0, len(lst)):
	for j in range(i+1, len(lst)):
		if lst[i]+lst[j] == n:
			lst_z.append(lst[i])
			lst_z.append(lst[j])
print(*lst_z)

