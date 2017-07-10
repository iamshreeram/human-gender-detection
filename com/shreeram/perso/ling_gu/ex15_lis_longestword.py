import time

#Compare word and word length
#Get the list of words
def get_words():
    word_count = int(raw_input("Enter the number of words : "))
    word_lis = []
    for i in range(word_count):
        word = raw_input("Enter the words %d: " %(i+1))
        word_lis.append(word)        
    #word_lis = ''.join(word_lis)
    return word_lis

#Calculating length of words in list
def cal_length(list_words):
    word_leng = [] #Creating list to send length
    for i in list_words:
        word_length = len(i)
        word_leng.append( word_length )
    return word_leng

#Map the words count to list of length
def zip_word_length(list_words,word_length):
    dictionary = dict(zip(list_words,word_length))
    return dictionary

#Pulling longest word 
def longest_zipped(zipped_length):
    v=list(zipped_length.values())
    k=list(zipped_length.keys())
    return k[v.index(max(v))]

list_words = get_words()
len_count = len(list_words)
word_length = cal_length(list_words)
zipped_length = zip_word_length(list_words,word_length)
longest_zip_value = longest_zipped(zipped_length)

print "Longest word in your file is : %s" % longest_zip_value
