class Calculator:

    def calculate(self, a: float, b: float, operation: str) -> float:
        operation = operation.lower()

        if operation in ["add", "addition"]:
            return a + b

        elif operation in ["sub", "subtract", "subtraction"]:
            return a - b

        elif operation in ["mul", "multiply", "multiplication"]:
            return a * b

        elif operation in ["div", "divide", "division"]:
            if b == 0:
                print("Error: Cannot divide by zero!")
                return None
            return a / b

        else:
            print("Invalid operation type!")
            return None


# Example usage
calc = Calculator()

a = 10.5
b = 2.5
operation = "add"

result = calc.calculate(a, b, operation)
print("Result:", result)
