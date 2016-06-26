#Histogram printing

def histogram(lines):
    for line in lines:
        temp = []
        for i in range(line):
            temp.append("*")
        charset = ''.join(temp)
        print charset 

lines1 = int(raw_input("Enter the number 1 : "))
lines2 = int(raw_input("Enter the number 2 : "))
lines3 = int(raw_input("Enter the number 3 : "))
lines=lines1,lines2,lines3
print lines
histogram(lines)
