#Luis Emmanuel Mendez Barrios
#2022/06/08

def toLowerCase(word):
    return word.lower()

def countWords(phrase,case_sensitive=False):
    if(len(phrase) == 0):
        return 0
    words = phrase.split()

    if not case_sensitive:
        words = map(toLowerCase,words)
    
    count_words = {} 
    for word in words:
        count_words[word] = (count_words.get(word) or 0 ) + 1  
    return count_words

phrase = input()
print(countWords(phrase,True))
