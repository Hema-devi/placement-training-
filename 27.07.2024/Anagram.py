

from collections import Counter

def anagram(word, myList):
    word = word.lower()
    anagrams = []
    for words in myList:
    	if word != words.lower():
    		if Counter(word) == Counter(words.lower()):
    			anagrams.append(words)
    return anagrams

if __name__ == '__main__':
    print(anagram("ant", ["tan", "stand", "at"]))                               
    print(anagram("master", ["stream", "pigeon", "maters"]))                   
    print(anagram("good", ["dog", "goody"]))                                
    print(anagram("allergy",[
            "gallery", "ballerina", "regally", "clergy", "largely", "leading"
        ]))     
    print(anagram("BANANA", ["Banana"]))                                      
