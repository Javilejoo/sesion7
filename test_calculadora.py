import pytest

from calculadora import square, factorial, is_prime, gcd, lcm


# ---------- square ----------
def test_square_positivo():
    assert square(4) == 16


def test_square_negativo():
    assert square(-3) == 9


def test_square_cero():
    assert square(0) == 0


def test_square_decimal():
    assert square(2.5) == 6.25


# ---------- factorial ----------
def test_factorial_de_5():
    assert factorial(5) == 120


def test_factorial_de_1():
    assert factorial(1) == 1


def test_factorial_de_0():
    assert factorial(0) == 1


# ---------- is_prime ----------
def test_is_prime_con_primos():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(13) is True


def test_is_prime_con_no_primos():
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(15) is False


def test_is_prime_casos_especiales():
    assert is_prime(0) is False
    assert is_prime(1) is False


# ---------- gcd ----------
def test_gcd_basico():
    assert gcd(12, 18) == 6


def test_gcd_coprimos():
    assert gcd(7, 9) == 1


def test_gcd_con_cero():
    assert gcd(5, 0) == 5


# ---------- lcm ----------
def test_lcm_basico():
    assert lcm(4, 6) == 12


def test_lcm_coprimos():
    assert lcm(3, 5) == 15


def test_lcm_mismo_numero():
    assert lcm(7, 7) == 7


# ========== Casos de error ==========

# ---------- square ----------
def test_square_con_string_lanza_error():
    with pytest.raises(TypeError):
        square("4")


def test_square_con_none_lanza_error():
    with pytest.raises(TypeError):
        square(None)


def test_square_con_bool_lanza_error():
    with pytest.raises(TypeError):
        square(True)


# ---------- factorial ----------
def test_factorial_negativo_lanza_error():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_decimal_lanza_error():
    with pytest.raises(TypeError):
        factorial(2.5)


def test_factorial_con_string_lanza_error():
    with pytest.raises(TypeError):
        factorial("5")


def test_factorial_con_bool_lanza_error():
    with pytest.raises(TypeError):
        factorial(True)


# ---------- is_prime ----------
def test_is_prime_decimal_lanza_error():
    with pytest.raises(TypeError):
        is_prime(7.0)


def test_is_prime_con_string_lanza_error():
    with pytest.raises(TypeError):
        is_prime("7")


# ---------- gcd ----------
def test_gcd_decimal_lanza_error():
    with pytest.raises(TypeError):
        gcd(12.5, 5)


def test_gcd_con_string_lanza_error():
    with pytest.raises(TypeError):
        gcd(12, "6")


# ---------- lcm ----------
def test_lcm_ambos_cero_lanza_error():
    with pytest.raises(ValueError):
        lcm(0, 0)


def test_lcm_con_string_lanza_error():
    with pytest.raises(TypeError):
        lcm("4", 6)
