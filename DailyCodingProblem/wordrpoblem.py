from collections import defaultdict
from string import ascii_letters

def create_wordmap(dictionary):

    wordmap = defaultdict(list)
    for word in dictionary:
        print(tuple(sorted(word)))
        wordmap[tuple(sorted(word))].append(word)
    return wordmap

def step_words(word,dictionary):
    
    wordmap=create_wordmap(dictionary)
    step_words = []
    
    for letter in ascii_letters:
        key = tuple(sorted(word + letter))
        if wordmap[key]:
            step_words.extend(wordmap[key])
    return step_words


dict = ["TEAM","MEAT","APPLE", "APPEAL"]
print(step_words("APPLE",dict))