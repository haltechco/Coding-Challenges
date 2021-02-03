#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wednesday 20 January 2021.
Finished on
@author: h.
References:
https://projecteuler.net/about
"""
#------------------------------------------------------------------------------#
""" Question.
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
#------------------------------------------------------------------------------#
prime_factors = []

target = 600851475143
i = 2

while i*i <= target:  # itterating through to the largest prime factor
    if target % i:    # if the target divisible by i is not 0, execute
        i += 1        # add one to the prime factors being divised
    else:
        target //= i  # target divided by i is prime factor
        prime_factors.append(target)

print(prime_factors[-1])
