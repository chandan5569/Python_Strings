x=input('enter the string')

y=len(x)

if y>2:

  z = x[:2]  + x[y-2:]

  print(z)

elif y == 2:

  z = x[:2] + x[:2]

  print(z)

else:

  print('empty string')

