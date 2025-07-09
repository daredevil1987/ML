def sum(arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count

arr = [2, 7, 4, 1, 3, 6]
target = 10

result = sum(arr, target)
print(f"Number of pairs with sum {target}: {result}")
