from __future__ import annotations

# snippet: rational
class Rational:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def mult(self, other: Rational) -> Rational:
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

if __name__ == '__main__':
    first: Rational = Rational(2,3)
    second: Rational = Rational(4,5)
    print(first.mult(second))
# snippet: /rational
