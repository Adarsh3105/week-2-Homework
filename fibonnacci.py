# A program that displays Fibonacci numbers using people's names.

##Richella O'Driscoll Week 1 and Week 2 Exercises



#Week 1 Exercise- Fibonacci



def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



# Test the function with the following value.
x=int(input(""))
ans = fib(x)

print("Fibonacci number", x, "is", ans)



#Week 2 Exercise

# A program that displays Fibonacci numbers using people's names.



def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



#My name is Richella, then the first and last letter of my name give the number 19 (R+A = 19). The 19th Fibonacci number is 4181. 

name = "ODriscoll"

first = name[0]

last = name[-1]

firstno = ord(first)

lastno = ord(last)

x = firstno + lastno



ans = fib(x)

print("My surname is", name)

print("The first letter", first, "is number", firstno)

print("The last letter", last, "is number", lastno)

print("Fibonacci number", x, "is", ans)



#ord() method returns an integer representing the Unicode code point of the given Unicode character.
