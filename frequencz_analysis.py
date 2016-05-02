#!/usr/bin/python3

from collections import Counter
import itertools

def getTextClean(string):
    string=string.replace("\n","")   #get rid off breaks
    string=string.replace(" ","")   #get rid off spaces
    for char in symbols:
        string=string.replace(char, "")   #get rid off symbols
    string=string.lower()                  #get all lower case
    return string

def getMatchScore(freqOrder):
    freqOrder=''.join(freqOrder)
    matchScore=0
    for commonLetter in etaoin[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore+=1
    for uncommonLetter in etaoin[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore+=1
    return (matchScore,freqOrder)
    

def getItemAtIndexZero(x):
    return x[0]

def getTextSplit(text_strip):
    text_split=[text_strip[i:i+1] for i in range(0,len(text_strip),1)]
    return text_split

def getPerms(freqOrder):
    firstSix=freqOrder[:6]
    lastSix=freqOrder[-6:]
    firstPerm=list(itertools.permutations(firstSix))
    lastPerm=list(itertools.permutations(lastSix))
    return (firstPerm,lastPerm)

def getDecrypt(text_strip,totalKeys):
    decrypt=[]
    text_split=getTextSplit(text_strip)
    for Key in totalKeys:
        succes=0
        for symbol in text_split:
            if symbol in alphabet:
                pos=Key.index(symbol)
                decrypt.append(etaoin[pos])
         #      print(freqOrder.index(symbol),etaoin[pos])
        decrypt=''.join(decrypt)
        for word in keywords_en:
            if word in decrypt:
                succes+=1
                if succes==7:
                    print('8 Keywords match in', ': ', decrypt)
        decrypt=[]
    return decrypt
#TODO avoid all keys in memory by generating one key->decrypt->check for keywords (maybe longer keywords(5 chars))->repeat

#--------------------------------------------------------------------------------
englLetterFreq={'e':12.7, 't':9.06, 'a':8.17, 'o':7.51, 'i':6.97, 'n':6.75, 's':6.33, 'h':6.09, 'r':5.99, 'd':4.25, 'l':4.03, 'c':2.78, 'u':2.76, 'm':2.41, 'w':2.36, 'f':2.33, 'g':2.02, 'y':1.97, 'p':1.93, 'b':1.29, 'v':0.98, 'k':0.77, 'j':0.15, 'x':0.15, 'q':0.10, 'z':0.07}

etaoin='etaoinshrdlcumwfgypbvkjxqz'
alphabet='abcdefghijklmnopqrstuvwxyz'

keywords_en=['the','be','to', 'of', 'and', 'in', 'that', 'have', 'it', 'for'] 
symbols='`\',.;:?!"&%#*’” “-+'

#string='yvdxgjhv hzrevg bswf esch lw ycuokbj jqf pi vcr epr hzgfb okbg sh oqmooo aqioh ds imps ist ab tnoqw hcu xjs zigyhrf'
#string='vjku ycu tkejctf hgapocp pgctkpi vjg etguv qh jku rqygtu. cv vygpva-vjtgg ... vjgtg ycu pq rjaukekuv qp gctvj yjq eqwnf ocvej jku gzwdgtcpv eqoocpf qxgt vjg pcvkxg ocvgtkcnu qh vjgqtgvkecn uekgpeg. kv ycu pqv lwuv c hceknkva cv ocvjgocvkeu (vjqwij kv jcf dgeqog engct ... vjcv vjg ocvjgocvkecn ocejkpgta gogtikpi htqo vjg yjggngt–hgapocp eqnncdqtcvkqp ycu dgaqpf yjggngtu qyp cdknkva). hgapocp uggogf vq rquuguu c htkijvgpkpi gcug ykvj vjg uwduvcpeg dgjkpf vjg gswcvkqpu, nkmg cndgtv gkpuvgkp cv vjg ucog cig, nkmg vjg uqxkgv rjaukekuv ngx ncpfcw—dwv hgy qvjgtu.'
relative_frequency={}
totalKeys=[]
newFreqOrder={}
freqToLetter={}
f=open('textrot','r')
text_strip=f.read()
text_strip=getTextClean(text_strip)

#count the occurence of letters
frequency=Counter(text_strip)
sorted(frequency.items(), key=lambda pair:pair[1], reverse=True)
#print(frequency)

#sort the letters to a special frequency
for letter in alphabet:
    if frequency[letter] not in freqToLetter:
        freqToLetter[frequency[letter]]=[letter]
    else:
        freqToLetter[frequency[letter]].append(letter)

#put each list of letters in reverse etaoin order and convert into a string
for freq in freqToLetter:
    freqToLetter[freq].sort(key=etaoin.find, reverse=True)
    freqToLetter[freq]=''.join(freqToLetter[freq])

#pair letter and frequency
freqPairs=list(freqToLetter.items())
freqPairs.sort(key=getItemAtIndexZero, reverse=True)

#extract letters for final string
freqOrder=[]
for freqPair in freqPairs:
    freqOrder.append(freqPair[1])

freqOrder=''.join(freqOrder)

#get permutations of the first and last six elements of the order of the analysis
permEtaoin,permVkjxqz=getPerms(freqOrder)

#decrypt the text with the different possible permutations
#join together the new decypher key (720^2 in total) and list them in totalKeys
centralLetters=freqOrder[6:-6]
centralLetters=''.join(centralLetters)
for perms1 in permEtaoin:
    perms1=''.join(perms1)
    for perms2 in permVkjxqz:
         perms2=''.join(perms2)
         totalKeys.append(perms1+centralLetters+perms2)
decrypt=getDecrypt(text_strip,totalKeys)

print('Finished Decrypting')
