def is_prime(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  
  return True


print(is_prime(2))
print(is_prime(7))
print(is_prime(10))
