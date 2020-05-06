mynumber = int(input("Up too what number?"))
n1, n2 = 0, 1
count = 0
if mynumber <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   while n1 < mynumber:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth