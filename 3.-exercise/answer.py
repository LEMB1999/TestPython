#Luis Emmanuel Mendez Barrios
#2022/06/08

#convert the word to lowercase
def toLowerCase(word):
    return word.lower()


def countWords(phrase,case_sensitive=False):

    #validate that the param passed to function is a string
    if not isinstance(phrase,str):
        return "the {0} is not a string".format(phrase)

    if(len(phrase) == 0):
        return {}

    #divided the words and save them in a list
    words = phrase.split()

    #check if the user want to difference in case sensitive
    if not case_sensitive:
        words = map(toLowerCase,words)
    
    count_words = {} 
    for word in words:
        count_words[word] = (count_words.get(word) or 0 ) + 1  
    return count_words

#phrase = input()
#print(countWords(phrase,True))
