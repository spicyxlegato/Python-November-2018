# List manipulation.
# Can use either += operator or extend() method.

m = [1,2,3]
n = [4,5,6]
print(m)
print(n)
k = m + n
print(k)

k += [7,8,9]
print(k)

k.extend([10,11,12,13,14])
print(k)

k.reverse()
print(k)

h = "not perplexing do handwriting family where I illegibly know doctors".split()
print(h)

# Sort the elements by length.
h.sort(key=len)
print(h)

# Join them into a single string again.
h = ' '.join(h)
print(h)

# Reverse the list assigned to variable p without modifying it.
p = [9, 3, 1, 0]
q = reversed(p)
print(list(q))