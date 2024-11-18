# This is a small python program that declares a function
# cb that takes the argument i from the for loop. The for loop
# takes a range of numbers 0-19, performs division by 2 
# if there is a remainder (odd) is passed to cb where the number is
# cubed. An example invocation is python3 cube.py

def cb(i):
  return i**3
  
for i in range(19):
  if i % 2 != 0:
    x = cb(i)
    print(x)
