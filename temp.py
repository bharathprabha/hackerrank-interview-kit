arr = [1, 2, 3, 4, 5, 6]
i = 1
j = 4
swap = 0
for i in range(j, i - 1, -2):
    (arr[i], arr[i-1]) = (arr[i-1], arr[i])
    swap += 1
print(arr, swap)
