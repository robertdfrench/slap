# This function is non-linear because it is not additive:
def f(x):
    return x + 3

print(f(8) + f(10))
print(f(8 + 10))


# This function is not linear because it is not homogeneous:
def g(x):
    return x * x

print(8 * g(10))
print(g(8 * 10))


# Mathematically speaking, the following function is linear. But
# remember that we are not dealing with a field, since addition
# is not additive on computers. Show that there are values for
# a, x, and y such that a * h(x + y) != h(a*x + a*y)
def h(x):
    return x

# Solution:
# a = 10000000000
# x = 0.0000000001234567
# y = 0.0000000009
# print(a * h(x + y))
# print(h(a*x + a*y))
