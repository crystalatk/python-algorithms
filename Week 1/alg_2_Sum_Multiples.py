# 2. Sum of All Multiples of 3 or 5 below 1000
# # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# # Find the sum of all the multiples of 3 or 5 below 1000.

r = 0
for n in range(1,1001):
    a = 3
    b = 5
    if n % a == 0 or n % b == 0:
        r += n
print(r)