def square(n):
    """Retorna el cuadrado de un número."""
    return n * n


def factorial(n):
    """Retorna el factorial de un número entero positivo."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def is_prime(n):
    """Retorna True si el número es primo, False si no lo es."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """Retorna el máximo común divisor de dos números (algoritmo de Euclides)."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Retorna el mínimo común múltiplo de dos números."""
    return a * b // gcd(a, b)
