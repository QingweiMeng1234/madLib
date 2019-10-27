import os,re
#open file
file = open('Test.txt','r')
text = file.read()
#make a list to contain words.
strlist = text.split()
#make a dictionary to store words end with a punctuation and print out the list without punctuations.
dic = {}
i = 0
for words in strlist:
    if ',' in words or '.' in words or '!' in words or '?' in words:
        dic[i] = words
        strlist[i] = words[:-1]
    i += 1

print('the strlist is: ')
print(strlist)
print('the dictionary is: ')
print(dic)    

#find out where to replace

#findall accepts two parameters. The first one is the regex, the second one is the targeted text. Return a list of strings.
replist = re.findall(r'[A-Z]{2,}',text)   
for rep in replist:
    if rep[0] in 'AEIOU':
        inputstr = input('Enter an %s'%rep.lower())
    else:
        inputstr = input('Enter a %s'%rep.lower())
    strlist.insert(strlist.index(rep),inputstr)
    strlist.remove(rep)
#add up the punctuations recorded in the dictionary.
for k,v in dic.items():
    strlist[k] += str(v[-1])  
#create new file to put words in
file2 = open('Testresults.txt','w')
result = ''
for words in strlist:
    file2.write(words+' ')
    result += words + ' '

print(result)
#close file
file2.close()

    



