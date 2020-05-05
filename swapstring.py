x='abc','xyz'

y=x[0]

z=x[1]

a=y[:2]

b=z[:2]

w= b+y[2:]

v=a+z[2:]

s=w+' '+v
print(s)
