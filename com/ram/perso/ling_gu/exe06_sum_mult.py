#import math
#This program get list of numbers to sum up or multiply

print "############################################"
print "Enter list of numbers to sum up or multiply"
print "###########################################"

def sumo(list_num):
    sum_temp=0
    for sum_num in list_num:
        sum_temp=sum_temp+sum_num
    print sum_temp

def multiply(list_num):
    mul_temp=1
    for mul_num in list_num:
        mul_temp=mul_temp*mul_num
    print mul_num

num = raw_input("Enter the list of numbers : ")
list_num = list(num)
sumo(list_num)
multiply(list_num)
