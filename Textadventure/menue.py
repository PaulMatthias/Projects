#!/usr/bin/python3
import actions
import maps
import gameobjects

def start_menue():
    print('#'*50)
    print('\n')
    print('                     Die Herrschaft des Riesenzwergs\n')
    print('\n')
    print('Willkommen zu dem spannendsten Abenteuer seit "Day of the Tentacle"!!! \n')
    print('Eine Herausforderung an den Grafikverwoehnten Gamer von heute. \n')
    print('Nur jetzt und heute, spiele dieses einzigartige Textandventure. \n')
    print('Der einzige Controller ist deine Tastatur und dein Kopf deine Grafikkarte. \n')
    print('#'*50)
    print('\n')
    print('Menue:\n')
    print('1) Start [Startet das Spiel von Anfang an]\n')
    print('2) Laden [Laedt ein gespeichertes Spiel]\n')
    print('3) Exit [Verlaesst das Spiel]\n')
    print('\n')
    print('Gib "Hilfe" jederzeit ein um die wesentlichen Befehle gezeigt zu bekommen\n')
    
    while True:
        option=get_start_input()
        if option=='chosen':
            break
    
    while True:
        get_input()

def get_input():
    command=input(": ").split()
    verb_word = command[0]
    if verb_word in actions.verb_dict:
        verb = actions.verb_dict[verb_word]
    else:
        print("Unbekannter Befehl {}". format(verb_word))
        return

    if len(command) >=2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())



def get_start_input():
    command=input(": ").split()
    verb_word = command[0]
    if verb_word in start_dict:
        verb = start_dict[verb_word]
    else:
        print("Unbekannter Befehl {}". format(verb_word))
        return

    if len(command) >=2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())

    if verb_word=="Start":
          option='chosen'
          return option

def start():
    print('\n')
    print('Willkommen in der Welt Grubmah!\n')
    print('In dieser Welt geschieht alles nur mit der richtigen Eingabe deiner Befehle.\n')
    print('\n')
    print('Der boese arbeitslose Riesenzwerg Knarf hat das ganze Land unterjocht, fast niemand ist mehr uebrig geblieben.\n')
    print('In diesem verkommenen Land lieferte insbesondere eine Familie Widerstand: Die Murasa.\n')
    print('Jahrelang bekaempften sie die Schreckensherrschaft von Knarf, bis sie schliesslich alle untergingen.\n')
    print('\n')
    print('Alle bis auf Einen.\n')
    print('\n')
    print('Du bist die letzte Hoffnung von Grubmah.\n')
    print('Ziehe los und stuerze den arbeitslosen Riesenzwerg!\n')
    print('Dein Abentuer beginnt in einer Gefaengniszelle unter dem Schloss Knarfs.\n')
    print('\n')
    print('Dies ist dein Geschichte!\n')
    print('\n')
    while True:
        get_input()

def stop():
    exit()

def helpme():
    print('\n')
    print("Die wichigsten Befehle:\n")
    print("'sag #Eingabe': sage irgendetwas\n")
    print("'gehe nord/ost/sued/west': bewege dich auf der Karte\n")
    print("'oeffne #Eingabe': oeffnet Gegenstaende\n")
    print("'schlage #Eingabe': Kampf mit Gegner\n")
    print("'untersuche #Eingabe': untersucht Gegenstand oder Person\n")
    print("'position': Gibt deine aktuelle Position in Form von Koordinaten wieder\n")
    print("'exit': Verlaesst das Spiel")

start_dict={
        "Start":start,
    #       "Laden":load,
        "Exit":stop,
        "Hilfe":helpme,
        }
