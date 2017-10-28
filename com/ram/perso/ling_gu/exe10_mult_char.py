import sys
#Character multiplication with out * in Python

#Checks if its single character
def charsize(x):
    if len(x) == 1:
        return True
    else:
        return False

#To get the count 
def get_count():
    char_count = raw_input("Enter count to repeat : ")
    return char_count


#Gets character 
def get_char():
    char = raw_input("Enter a character to enter : ")
    return char

#Generate characters 
'''
    else:
        char_count = get_count()
'''        


def generate_n_chars(char,n):
    temp = []
    for i in range(int(n)): 
        temp.append(char)
        charset = ''.join(temp)
    return charset

char = get_char()
size_check = charsize(char)
if size_check == False:
    print "Please enter single character. Exiting application..."
    sys.exit()

n = get_count()
char_set = generate_n_chars(char,n)
print char_set
