#!/usr/bin/python3

#text = 'sg kof swbaoz gqvcsbs uswgvo boasbg robw'
#text='aa ab ac ad ae ba bb bc bd be ca cb cc cd ce da db dc dd de ea eb ec ed ee'
text='1424154315422531114244155344244344241544554455455115424313233145154343153133'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_25 = 'abcdefghiklmnopqrstuvwxyz'
alphabet_25_split=[alphabet_25[i:i+1] for i in range(0,len(alphabet_25),1)]

#-----ROT-Verschiebung------------------------------------------------

def rot_verschiebung(text):
    text_split=text.split()

    words=len(text_split)

    print('ROT-Verschiebung:')
    for move in range(0,26):
        decoded=""
        for word in range(0,words):
            new_text= ''.join((chr(97+(ord(letter)-97+move)%26) for letter in text_split[word]))
            decoded= decoded + ' ' + new_text
        print (move, ':', decoded)

#--------------------------------------------------------------------


#---square chiffre--------------------------------------------

def square_chiffre(text,pw1,pw2):

    print('\n Polybios chiffre (square)')

    matrix=''
    decrypt=''
    text_strip=text.replace(" ","")   #get rid off spaces
    words=len(text_strip)
    
    #Password and text split
    pw1_split=[pw1[i:i+1] for i in range(0, 5, 1)]
    pw2_split=[pw2[i:i+1] for i in range(0, 5, 1)]
    text_split=[text_strip[i:i+2] for i in range(0, len(text_strip), 2)]

    #Matrix aufstellen
    for i in range(0,len(pw1)):
        for j in range(0,len(pw2)):
            matrix+=pw1_split[i] + pw2_split[j]
    
    matrix_split=[matrix[i:i+2] for i in range (0,len(matrix), 2)]

    #decrypting
    for i in range(0,len(text_split)):
        for j in range(0,len(matrix_split)):
            if text_split[i]==matrix_split[j]:
                decrypt+=alphabet_25_split[j]
    
    print(decrypt)
#-------------------------------------------------------------

#TODO add vigeniere chiffre
#TODO add if clauses to neglect unimportant chiffre (eg rot shift for numbers etc)


rot_verschiebung(text)
square_chiffre(text,'12345','12345')
