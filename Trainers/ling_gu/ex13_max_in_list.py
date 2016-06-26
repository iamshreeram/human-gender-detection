

def max_in_list(lis):
    maximum  = max(lis)
    print "Maximum number is ", maximum


count = int(raw_input("Enter the number counts you need : "))
lis = []
for i in range(count):
    num = int(raw_input("Enter the value :"))
    lis.append(num)

print lis
max_in_list(lis)
