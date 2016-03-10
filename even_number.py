from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prime_check(n):
  if n in prime_check.not_primes:
    return False
  if n in prime_check.primes:
    return True

  if is_prime(n):
    prime_check.primes.add(n)
    return True
  else:
    prime_check.not_primes.add(n)
    return False
prime_check.primes = set()
prime_check.not_primes = set()
    
def genBreakdown(num):
  for n in range(3, int(num/2), 2):
    yield[n, num -n]
  
def check_num(num):
  breakdowns = genBreakdown(num)
  for p in breakdowns:
    if not(prime_check(p[0]) or prime_check(p[1])):
      return False
  return True

# find the largest even number under upperbound, which can't be composed
# by adding 2 non-prime odd numbers
def find_target_number(upperBound = 200):
  upperBound -= upperBound % 2
  for num in range(upperBound, 2, -2):
    if check_num(num):
        print("found target even number: {}".format(num))
        break

find_target_number()
#print("prime: {}".format(", ".join(str(x) for x in prime_check.primes)))
#print("not prime: {}".format(", ".join(str(x) for x in prime_check.not_primes)))


