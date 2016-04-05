#!/usr/bin/python3

text = 'sg kof swbaoz gqvcsbs uswgvo boasbg robw'

#-----ROT-Verschiebung------------------------------------------------

def rot_verschiebung(text):
    text_split=text.split()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    words=len(text_split)

    print('ROT-Verschiebung:')
    for move in range(0,26):
        decoded=""
        for word in range(0,words):
            new_text= ''.join((chr(97+(ord(letter)-97+move)%26) for letter in text_split[word]))
            decoded= decoded + ' ' + new_text
        print (move, ':', decoded)

#--------------------------------------------------------------------

rot_verschiebung(text)
