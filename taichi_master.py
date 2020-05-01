"""
Group: Tai-Chi
Leader: Riley Sherwood
Engineers: Scott Murray, Josh Barkley, Aaron Lim
CSE408: Fadi
Spring 2020
Lab4: Version Control System
GitHub-advanced
Due: Tuesday May 5th 6:00 pm
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
###############################################################################
print("Begin problem 3-C (Riley)")
"""
c. Write a program containing a function to convert the current time, into military
time.
"""  
###############################################################################

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:04:19 2020

@author: woods
"""


# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("08:05:45 PM")) 


print("###########################################");
###############################################################################
print("Begin problem 3-D (Josh)")
"""
d. Write a program containing a function to output the fibonacci sum up to a user
inputted number.
"""  
###############################################################################

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


print("###########################################");
###############################################################################
print("Begin problem 3-E (Scott)")
"""
e. Write a program containing a function to check if a user inputted string is a good
password or not, if not have them try again. A password is considered good if it
contains at least 7 characters and 2 of those are either a number or special
character(by special character I mean any one of the characters on the numbers
1-8, i.e. !@#$%^&*).
"""  
###############################################################################