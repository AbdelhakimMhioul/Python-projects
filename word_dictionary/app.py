from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter a word: ")
    print(dictionary.meaning(word))
