class MathUtil:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Using static methods
print(MathUtil.add(3, 5))  # Output: 8
print(MathUtil.multiply(3, 5))  # Output: 15

# You can also use an instance of the class to call static methods, although it's less conventional
math = MathUtil()
print(math.add(3, 5))  # Output: 8
print(math.multiply(3, 5))  # Output: 15
