from abc import ABC, abstractmethod

# Abstract base class for operations
class Operation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

# Concrete classes for each operation
class Addition(Operation):
    def calculate(self, a, b):
        return a + b

class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b

class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b

class Division(Operation):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Calculator class using operations
class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def execute_operation(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"Operation '{name}' not supported")
        return self.operations[name].calculate(a, b)

# Usage
calculator = Calculator()
calculator.add_operation("add", Addition())
calculator.add_operation("subtract", Subtraction())
calculator.add_operation("multiply", Multiplication())
calculator.add_operation("divide", Division())

print(calculator.execute_operation("add", 5, 3))       # Output: 8
print(calculator.execute_operation("subtract", 5, 3))  # Output: 2
print(calculator.execute_operation("multiply", 5, 3))  # Output: 15
print(calculator.execute_operation("divide", 5, 3))    # Output: 1.666...
