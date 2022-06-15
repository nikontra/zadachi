def merge(arr, lf, mid, rg):
	n = r = 0
	k = lf
	left = arr[lf:mid]
	right = arr[mid:rg]
	while n < len(left) and r < len(right):
		if left[n] <= right[r]:
			arr[k] = left[n]
			n += 1
		else:
			arr[k] = right[r]
			r += 1
		k += 1
	# if lf + n < mid:
	# 	while k < rg:
	# 		arr[k] = left[n]
	# 		n += 1
	# 		k += 1
	# else:
	# 	while k < rg:
	# 		arr[k] = right[r]
	# 		r += 1
	# 		k += 1
	# return arr

	while n < len(left):
		arr[k] = left[n]
		n += 1
		k += 1
	while r < len(right):
		arr[k] = right[r]
		r += 1
		n += 1
	return arr


def merge_sort(arr, lf, rg):
	if (rg - lf) <= 1:
		return

	midle = (lf + rg) // 2
	# print(midle, arr[midle])
	merge_sort(arr, lf, midle)
	merge_sort(arr, midle, rg)
	merge(arr, lf, midle, rg)


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0, 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

x = [18, -19, 15, -8, 14, 6, -6, 8, 17]
merge_sort(x, 0, len(x))
print(x)
