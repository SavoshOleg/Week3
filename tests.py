def add(x, y):
    """Додає два числа."""
    return x + y

def subtract(x, y):
    """Віднімає два числа."""
    return x - y

def multiply(x, y):
    """Множить два числа."""
    return x * y

def divide(x, y):
    """Ділить два числа."""
    if y == 0:
        raise ValueError('Ділення на нуль неможливе')
    return x / y
