# This is a small python program that declares a function
# sq that takes the argument i from the for loop and squares the numbers. 
# The for loop takes a range of numbers 0-19 and parses through them by 1 
# the numbers are passed to sq and are squared and printed. 
# An example invocation is python3 square.py
def sq(i):
  return i**2
  
for i in range(19):
  x = sq(i)
  print(x)
