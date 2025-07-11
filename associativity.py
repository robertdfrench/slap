# In Python, numbers do not form a field. In particular,
# addition is not always associative.

# Consider the following list with numbers of differing
# magnitudes. Depending on the order in which we add the
# numbers, we get different results
a = [
    100000, 
    10000, 
    1000, 
    100, 
    10, 
    1, 
    0.1, 
    0.01, 
    0.001, 
    0.0001,
    0.00001
]

# ((((a[0] + a[1]) + a[2]) + a[3]) + ... )
print(sum(a))

# a[0] + (a[1] + (a[2] + (a[3] + ...)))
print(sum(reversed(a)))
