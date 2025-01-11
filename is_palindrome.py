'''Write a function is_palindrome() that checks whether a given string is a palindrome (i.e., it reads the same forwards and backwards). 
The function should return True if the string is a palindrome and False otherwise. 
Test the function with the string "racecar"stubborn.attack()
'''

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        print(s[::-1])
        return False
    
print(is_palindrome("dahl"))




