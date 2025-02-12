class Matrix:
    def __init__(self, arr2D):
        self.data = arr2D

    def shape(self):
        return (len(self.data), len(self.data[0]))

    def __str__(self):
        result = []
        for row in self.data:
            result.append("\t".join(map(str, row)))
        return "\n".join(result)

    def __repr__(self):
        return f"Matrix({self.data})"

    def __mul__(self, other):
        if isinstance(other, Matrix):
            r1, c1 = self.shape()
            r2, c2 = other.shape()
            if c1 == r2:
                output = []

                for i in range(r1):
                    output.append([])
                    for j in range(c2):
                        output[i].append(0)
                        for k in range(c1):
                            output[i][j] += self.data[i][k] * other.data[k][j]

                return Matrix(output)
            else:
                raise Exception(
                    f"Matrix shapes doesn't match {self.shape()} and {other.shape()}"
                )
        else:
            raise TypeError(
                f"Cannot multiply Matrix with object of type {type(other).__name__}"
            )

    def transpose(self):
        output = []

        for i in range(self.shape()[1]):
            output.append([])
            for j in range(self.shape()[0]):
                output[i].append(self.data[j][i])

        return Matrix(output)
