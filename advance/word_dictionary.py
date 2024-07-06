from PyDictionary import PyDictionary

word = input("Enter the word: ")
try:
    dictionary = PyDictionary(word)
    print(dictionary.printMeanings())
except ValueError:
    print("Invalid word")