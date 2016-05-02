#!/usr/bin/python3

#text = 'sg kof swbaoz gqvcsbs uswgvo boasbg robw'   #bsp fuer rot verschiebung
#text='aa ab ac ad ae ba bb bc bd be ca cb cc cd ce da db dc dd de ea eb ec ed ee' #bsp fuer square (polybius)
#text='1424154315422531114244155344244344241544554455455115424313233145154343153133' #bsp fuer caesarquadrat
#text='twwnp zoaas wnuhz bnwwg snbvc slypm m'  #bsp fuer vigener, pw HOUGHTON
text='kt tz zk wb xl ow ov kz kd lo po ur n' # BSP fuer playfair


#TODO fix that it is only working for no capital letters
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_25 = 'abcdefghiklmnopqrstuvwxyz'

#split abc 
alphabet_25_split=[alphabet_25[i:i+1] for i in range(0,len(alphabet_25),1)]

keywords_ger=['die','der','das','und','in', 'zu', 'ich', 'hab', 'werd', 'sie', 'von', 'mit']  
keywords_en=['the','be','to', 'of', 'and', 'in', 'that', 'have', 'it', 'for'] 

#set language for spell checker
keywords=keywords_ger

#-----ROT-Verschiebung------------------------------------------------

def rot_verschiebung(text):
    text_split=text.split()

    succes=0
    words=len(text_split)

    print(' ROT-Verschiebung:')
    for move in range(0,26):
        decoded=""
        for word in range(0,words):
            new_text= ''.join((chr(97+(ord(letter)-97+move)%26) for letter in text_split[word]))
            decoded= decoded + ' ' + new_text
        #check for most common keywords
        for key in range (0,len(keywords)):
            if keywords[key] in decoded:
                print(move,'match with', keywords[key], ': ', decoded)
                succes=1
    if succes==0:
        print('no match with keywords')
      #  print (move, ':', decoded)

#--------------------------------------------------------------------


#---square chiffre--------------------------------------------

def square_chiffre(text,pw1,pw2):

    print('\n Polybios chiffre (square)')

    matrix=''
    decrypt=''
    succes=0
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
    #check for most common keywords
    for key in range (0,len(keywords)):
        if keywords[key] in decrypt:
            print('match with', keywords[key], ': ', decrypt)
            succes=1
    if succes==0:
        print('no match with keywords')
#-------------------------------------------------------------

#--Vigenere chiffre-------------------------------------------

def vigenere(text,pw):
    print('\nVigenere cipher')
    decode=''
    text_strip=text.replace(" ","")   #get rid off spaces
    pw_split=[pw[i:i+1] for i in range(0, len(pw), 1)]
    text_split=[text_strip[i:i+1] for i in range(0, len(text), 1)]
     
    for letter in range(0,len(text_strip)):
        i= letter%len(pw)
        shift=alphabet.index(text_split[letter])- alphabet.index(pw_split[i])
        if shift < 0:
            shift+=26
        decode+=alphabet[shift]
    print('Decoded with password',pw,':',decode)
#-------------------------------------------------------------


#-Playfair Cypher --------------------------------------------

def playfair(text, key):
    print('\nPlayfair cipher')
    temp=[]
    new_key=[]
    decrypt=[]
    decode=''
    add_letter=0

    text_strip=text.replace(" ","")   #get rid off spaces

    #get an even amount of letters and split them into pairs
    if len(text_strip)%2==1:
        text_strip=text_strip+'a'
        add_letter=1
    text_split=[text_strip[i:i+1] for i in range(0, len(text_strip), 1)]

    #for i in range(0,len(text_split)-1):
        #      if text_split[2*i+1]==text_split[2*i]:   #TODO find a rule for the exception of double letters
  
 
    #split key and remove double letters
    key_split=[key[i:i+1] for i in range(0,len(key), 1)]   
    for i in range (0,len(key_split)): 
        if key_split[i] not in temp:
            new_key[len(new_key):]=key_split[i]
        temp[len(temp):]=key_split[i]

    #reduce alphabet by key letters and add key  in front
    for i in range(0, len(new_key)):
        alphabet_25_split.remove(new_key[i])
    new_key+=alphabet_25_split

    #check which of the three cases applies for the letter pairs if key would be aligned in a 5x5 matrix
    #1) in one column 2) in one row 3) not at all correlated
    for i in range(0,len(text_split), 2):
        pos1= new_key.index(text_split[i])
        pos2= new_key.index(text_split[i+1])

        if pos1%5==pos2%5:                              #criteria for columns
            if pos1>=5:
                pos1-=5
            else:
                pos1+=20
            if pos2>=5:
                pos2-=5
            else: 
                pos2+=20
            decrypt.append(new_key[pos1])
            decrypt.append(new_key[pos2])
            
        elif abs(pos1-pos2)<4:                            #criteria for rows
            if pos1%5==0:
                pos1+=4
            else:
                pos1-=1
            if pos2%5==0:
                pos2+=4
            else:
                pos2-=1
            decrypt.append(new_key[pos1])
            decrypt.append(new_key[pos2])

        else:                                           #everything else
            temp1=pos1//5*5+pos2%5
            temp2=pos2//5*5+pos1%5
            decrypt.append(new_key[temp1])
            decrypt.append(new_key[temp2])
        
    #remove additional letter again and align the decrypted list to a string
    if add_letter==1:
        decrypt.pop()
    for i in range(0,len(decrypt)):
        decode+=decrypt[i]
    print('Decoded with password',key,':',decode)
#-------------------------------------------------------------

#TODO add if clauses to neglect unimportant chiffre (eg rot shift for numbers etc)


rot_verschiebung(text)
square_chiffre(text,'12345','12345')
vigenere(text,'houghton')
playfair(text,'butzelbaer')
