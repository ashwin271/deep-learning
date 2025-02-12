from matrix import Matrix

x = [[1, 1, 1], [2, 2, 2]]

y = Matrix(x)

print(y)

print(y.shape())

z = y.transpose()

print(z)
