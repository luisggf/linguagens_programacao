def multiplicar_matrizes(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

resultado = multiplicar_matrizes(A, B)
print(resultado)
