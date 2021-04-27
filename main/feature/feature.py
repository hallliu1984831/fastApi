#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    for n in primes():
        if n < 1000:
            print (n)
        else:
            break

def is_odd(n):
    return n % 2 == 1

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
        
def _not_divisible(n):
    return lambda x: x % n > 0
  
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == "__main__":
    main()       
#result = list(filter(_not_divisible(), _odd_iter())  
#result = list(filter(is_odd, [1,2,4,5,6,9,10,15]))
#print(result)