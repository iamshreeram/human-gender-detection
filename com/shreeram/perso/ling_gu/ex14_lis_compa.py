import time

#Compare word and word length
#Get the list of words
def get_words():
    word_count = int(raw_input("Enter the number of words : "))
    word_lis = []
    for i in range(word_count):
        word = raw_input("Enter the words : ")
        word_lis.append(word)        
    #word_lis = ''.join(word_lis)
    return word_lis

#Get the list of word length
def get_lengths(len_count):
    len_lis = []
    for i in range(len_count):
        num = int(raw_input("Enter the length of words : "))
        len_lis.append(num)
    return len_lis

#Calculating length of words in list
def cal_length(list_words):
    word_leng = [] #Creating list to send length
    for i in list_words:
        word_length = len(i)
        word_leng.append( word_length )
    return word_leng

#Map the words count to list of length
def map_word_list(list_words,list_length):
    return True
    


print "############ This will map the list of words with its length ########"
list_words = get_words()
len_count = len(list_words)
list_length = get_lengths(len_count)

word_length = cal_length(list_words)
print word_length

map_word_list(list_words,list_length)
