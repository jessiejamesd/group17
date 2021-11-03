
""" program to print multiplication table """

try:

  multi = lambda x : x*num

  num = int(input("Enter a number:"))

  print("The multiplication table for",num,":")

  for i in range(1,11):

    print(i,"X",num,"=",multi(i))

except ValueError:

  print("Expecting a numeric value!")
