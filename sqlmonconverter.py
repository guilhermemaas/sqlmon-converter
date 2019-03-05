f = open('C:\\Users\\guilherme.maas\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt', 'r')

dict = {}
word = 'DATA IN'
wordcount = 0

for words in f.read().split():
    if word in words:
        wordcount =+ 1

print(f.read())
print(type(f))