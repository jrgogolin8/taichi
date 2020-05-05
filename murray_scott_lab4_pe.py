# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:36:08 2020

@author: scott

CSE 408 lab4 Part E
"""

pswd = input("enter your password: ")

#print(ord('!'))
#print(ord('A'))

def pswdStren (psw):
    specialChar = 0
    for i in psw:
        if 32 < ord(i) < 65:
            specialChar += 1
    if len(psw) < 7:
        print("password length is too small")
        return
    elif specialChar < 2:
        print("password too weak, please include two or more special characters or numbers")
        return
    else:
        print("password is strong")

pswdStren(pswd)