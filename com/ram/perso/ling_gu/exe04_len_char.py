#import math
#This program checks if the entered character is vowel or not.

print "#########################"
print "Enter any vowel"
print "#########################"

def find_length(str):
    le = len(str)
    print le
    return

def gett_input():
    str = raw_input("Enter the string : ")

str = raw_input("Enter the string : ")
    
if ((len(str)) == 1):
    if str in ('a', 'e', 'i', 'o', 'u'):
        print "Single character and vowel"
    else:
        print "Single character and not vowel"
else:
    print "Enter 1 character."
    gett_input()
