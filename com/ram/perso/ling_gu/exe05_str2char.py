#import math
#This program checks if the entered character is vowel or not.

print "######################################"
print "Enter any string to convert to swedish"
print "######################################"

def find_length(str):
    le = len(str)
    print le
    return

def gett_input():
    str = raw_input("Enter the string : ")


def translate (list_str):
    temp=""
    for word in list_str:
        if word in ('a', 'e', 'i', 'o', 'u'):
            new_word=word
        else:
            new_word=word+'o'+word
        temp = temp + new_word
    print temp.upper()


str = raw_input("Enter the string : ")
list_str = list(str.lower())
translate (list_str)



