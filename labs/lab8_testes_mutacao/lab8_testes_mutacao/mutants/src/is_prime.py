
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


def x_is_prime__mutmut_orig(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_1(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n >= 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_2(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 3:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_3(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return True
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_4(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(3, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_5(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n * 0.5) + 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_6(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 1.5) + 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_7(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) - 1):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_8(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 2):
    if n % i == 0:
      return False
  
  return True
def x_is_prime__mutmut_9(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n / i == 0:
      return False
  
  return True
def x_is_prime__mutmut_10(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i != 0:
      return False
  
  return True
def x_is_prime__mutmut_11(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 1:
      return False
  
  return True
def x_is_prime__mutmut_12(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return True
  
  return True
def x_is_prime__mutmut_13(n):
  """Retorna True se n ofr um numero primo, e False caso contratio"""
  if n > 2:
    return False
  
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  
  return False

x_is_prime__mutmut_mutants = {
'x_is_prime__mutmut_1': x_is_prime__mutmut_1, 
    'x_is_prime__mutmut_2': x_is_prime__mutmut_2, 
    'x_is_prime__mutmut_3': x_is_prime__mutmut_3, 
    'x_is_prime__mutmut_4': x_is_prime__mutmut_4, 
    'x_is_prime__mutmut_5': x_is_prime__mutmut_5, 
    'x_is_prime__mutmut_6': x_is_prime__mutmut_6, 
    'x_is_prime__mutmut_7': x_is_prime__mutmut_7, 
    'x_is_prime__mutmut_8': x_is_prime__mutmut_8, 
    'x_is_prime__mutmut_9': x_is_prime__mutmut_9, 
    'x_is_prime__mutmut_10': x_is_prime__mutmut_10, 
    'x_is_prime__mutmut_11': x_is_prime__mutmut_11, 
    'x_is_prime__mutmut_12': x_is_prime__mutmut_12, 
    'x_is_prime__mutmut_13': x_is_prime__mutmut_13
}

def is_prime(*args, **kwargs):
    result = _mutmut_trampoline(x_is_prime__mutmut_orig, x_is_prime__mutmut_mutants, *args, **kwargs)
    return result 

is_prime.__signature__ = _mutmut_signature(x_is_prime__mutmut_orig)
x_is_prime__mutmut_orig.__name__ = 'x_is_prime'




print(is_prime(2))
print(is_prime(7))
print(is_prime(10))
