class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b


math_operations_instance = MathOperations()
sum_of_numbers = MathOperations.add_numbers(10, 15)
print(f"Sum of Numbers: {sum_of_numbers}")
