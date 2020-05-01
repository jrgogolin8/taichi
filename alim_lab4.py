"""
Aaron Lim
CSE408: Fadi
Spring 2020
Lab4: Version Control System
GitHub-advanced
Due: Tuesday May 5th 6:00 pm
Problem #3: part A & B
"""
###############################################################################
print("Begin problem 3-B (Aaron)")  
"""
a. Write a program containing a function to reverse a user inputted string.

"""
###############################################################################

inputStr = input(str("Please enter a string to REVERSE: "));
print("String BEFORE reverse is: ");
print();

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

print("String AFTER reverse is: ", (reverse(inputStr)));
print();

print("###########################################");
###############################################################################
print("Begin problem 3-B (Aaron)")
"""
b. Write a program containing a function to check if a user inputted number is
prime.
"""  
###############################################################################
num = int(input("Enter a number: "));
  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num//2): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number")
   
print("###########################################");  