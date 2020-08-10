

b='ab'
c=b
print(id(b),id(c))
b+='cd'
print(id(b),id(c))
print(c is b)