#print any string reverse


def reverse(string):
    rev  = mystring[::-1]
    return rev.lower()


mystring = raw_input("Enter the string : ")
if(mystring == reverse(mystring)):
    print "%s is palindrome" %mystring
else:
    print "%s is not palindrome" % mystring
