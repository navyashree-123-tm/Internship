string="Hello Welcome to to Python Lab"
words=dict()
list=string.split(" ")
for word in list:
    if word in words:
        words[word]+=1
    else:
        words[word]=1
print(words)


            