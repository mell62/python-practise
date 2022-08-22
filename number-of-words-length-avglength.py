string=input("Enter the string:")
words=string.split(" ")
NumberOfWords=len(words)
print("Number of words in the string is:", NumberOfWords)
length=0
for word in words:
    length+=len(word)
print("Number of letters in string is:", length)
avgLength=length/NumberOfWords
print("Average length of a word in the string is:", avgLength)

