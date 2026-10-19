def _validar_numero(n):
    """Lanza TypeError si n no es un número (int o float)."""
    if isinstance(n, bool) or not isinstance(n, (int, float)):
        raise TypeError(f"Se esperaba un número, se recibió {type(n).__name__}")


def _validar_entero(n):
    """Lanza TypeError si n no es un número entero."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"Se esperaba un entero, se recibió {type(n).__name__}")


def square(n):
    """Retorna el cuadrado de un número."""
    _validar_numero(n)
    return n * n


def factorial(n):
    """Retorna el factorial de un número entero positivo."""
    _validar_entero(n)
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def is_prime(n):
    """Retorna True si el número es primo, False si no lo es."""
    _validar_entero(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """Retorna el máximo común divisor de dos números (algoritmo de Euclides)."""
    _validar_entero(a)
    _validar_entero(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Retorna el mínimo común múltiplo de dos números."""
    _validar_entero(a)
    _validar_entero(b)
    if a == 0 and b == 0:
        raise ValueError("El mcm no está definido cuando ambos números son 0")
    return a * b // gcd(a, b)
