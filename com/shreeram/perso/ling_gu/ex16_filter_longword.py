#Filter the long words
#get list of words
def get_words():
    word_count = int(raw_input("Enter the number of words : "))
    word_lis = []
    for i in range(word_count):
        word = raw_input("Enter the words : ")
        word_lis.append(word)        
    #word_lis = ''.join(word_lis)
    return word_lis

#get the threshold integer
def get_threshold():
    num = int(raw_input("Enter the threshold : "))
    return num

#Calculate list of length for all the words
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

#Pulling longest word and comparing
def longest_zipped(zipped_length):
    v=list(zipped_length.values())
    k=list(zipped_length.keys())
    # Find the longest word (value of word) 
    return k[v.index(max(v))]

#Filter the long words comparing with threshold
#def filter_long_words():


print "######### Filter the long words #############"
list_words = get_words()
get_threshold = get_threshold()
word_length  = cal_length(list_words)
zipped_length = zip_word_length(list_words,word_length)
longest_zip_value = longest_zipped(zipped_length)
print longest_zip_value
