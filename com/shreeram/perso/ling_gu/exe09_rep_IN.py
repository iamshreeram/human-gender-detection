#pass the list and a variable

'''
def reverse(string):
    rev  = mystring[::-1]
    return rev.lower()
'''

def charsize(x):
    if len(x) == 1:
        return True
    else:
        return False


def is_member(x,mylist_a):
    mylist_a_len = len(mylist_a)
    print "Length of the search string is : %d" %mylist_a_len
    for i in range(mylist_a_len):
        if x == mylist_a[i]:
            return True
        else:
            return False

    #With having IN condition 
    '''
    if x in mylist_a:
        print "true"
        return True
    else:
        print "false"
        return False
    '''

x = raw_input("Enter a value for X : ")
size_check = charsize(x)
if size_check == False:
    sys.exit("Please enter single character.Exiting out of application")

a = raw_input("Enter list of values for A : ")
mylist_a = list(a)
output = is_member(x,mylist_a)
if output == True:
    print "Matching string found in search population"
else:
    print "No match found in search population"
