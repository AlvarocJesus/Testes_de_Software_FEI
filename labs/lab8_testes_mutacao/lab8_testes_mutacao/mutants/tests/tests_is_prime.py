from src.is_prime import is_prime

def test_is_prime_basics():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def test_is_prime_advanced():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-7)