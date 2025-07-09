def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=A[i][k]*B[k][j]
    return result

def matrix_power(A, m):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    for _ in range(m):
        result = matrix_multiply(result, A)
    return result
A = [[1, 2],[3, 4]]
m = 3
result = matrix_power(A, m)
print(f"A^{m} =")
for row in result:
    print(row)
