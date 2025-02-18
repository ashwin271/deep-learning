class Dual:
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if isinstance(other, Dual):
            real = self.real + other.real
            dual = self.dual + other.dual
            return Dual(real, dual)
        return Dual(self.real + other, self.dual)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Dual):
            real = self.real - other.real
            dual = self.dual - other.dual
            return Dual(real, dual)
        return Dual(self.real - other, self.dual)

    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, Dual):
            real = self.real * other.real
            dual = self.real * other.dual + self.dual * other.real
            return Dual(real, dual)
        return Dual(self.real * other, self.dual * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Dual):
            if other.real == 0:
                raise ZeroDivisionError(
                    "Cannot divide with a dual number with zero real part."
                )
            real = self.real / other.real
            dual = (self.dual * other.real - self.real * other.dual) / (other.real**2)
            return Dual(real, dual)
        else:
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return Dual(self.real / other, self.dual / other)

    def __neg__(self):
        return Dual(-self.real, -self.dual)

    def __eq__(self, other):
        if isinstance(other, Dual):
            return self.real == other.real and self.dual == other.dual
        return False

    def __str__(self):
        return f"{self.real} + {self.dual}ε"

    def __repr__(self):
        return f"Dual({self.real}, {self.dual})"


def diff(f, x):
    return f(Dual(x, 1)).dual


if __name__ == "__main__":

    def f(x):
        return x * x + 3 * x + 5

    print(diff(f, 1))
