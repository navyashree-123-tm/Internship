#Write a Python program that takes a list of words and return the longest word and the length of the longest one
from functools import reduce
 
def longestLength(words):
    longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
    print("The word with the longest length is:", longest_word, " and length is ", len(longest_word))
  
a = ["one", "two", "third", "four"]
longestLength(a)