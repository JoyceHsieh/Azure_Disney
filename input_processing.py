import random
import math
import sys


def conv_sex(Sex):
    if Sex=='Male':
        Sex=1
    else:
        Sex=0

    return Sex

def  conv_bir(Birthday):

    return Birthday

def  conv_ZS(Zodiac):
    if Zodiac=='Aries':
        Zodiac=3
    elif Zodiac=='Taurus':
        Zodiac=4
    elif Zodiac=='Gemini':
        Zodiac=5
    elif Zodiac=='Cancer':
        Zodiac=6
    elif Zodiac=='Leo':
        Zodiac=7
    elif Zodiac=='Virgo':
        Zodiac=8
    elif Zodiac=='Libra':
        Zodiac=9
    elif Zodiac=='Scorpio':
        Zodiac=10
    elif Zodiac=='Sagittarius':
        Zodiac=11
    elif Zodiac=='Capricorn':
        Zodiac=12
    elif Zodiac=='Aquarius':
        Zodiac=1
    elif Zodiac=='Pisces':
        Zodiac=2

    return Zodiac


color_R=random.randint(0,255)


def  conv_EC(Eyes_color):
    EC=Eyes_color
    if EC=="Red":
        EC=[220,20,60]
    elif EC=="Pink":
        EC=[255,192,203]
    elif EC=="Orange":
        EC=[255,127,80]
    elif EC=="Gold":
        EC=[255,215,0]
    elif EC=="Purple":
        EC=[238,130,238]
    elif EC=="Green":
        EC=[50,205,50]
    elif EC=="Bule":
        EC=[135,206,235]
    elif EC=="Brown":
        EC=[165,42,42]
    elif EC=="White":
        EC=[255,255,255]
    elif EC=="Gray":
        EC=[128,128,128]
    elif EC=="Black":
        EC=[0,0,0]
    else:
        EC=[color_R,color_R,color_R]
    
    return EC



def  conv_HC(Hair_color):
    HC=Hair_color
    if HC=="Red":
        HC=[220,20,60]
    elif HC=="Pink":
        HC=[255,192,203]
    elif HC=="Orange":
        HC=[255,127,80]
    elif HC=="Gold":
        HC=[255,215,0]
    elif HC=="Purple":
        HC=[238,130,238]
    elif HC=="Green":
        HC=[50,205,50]
    elif HC=="Bule":
        HC=[135,206,235]
    elif HC=="Brown":
        HC=[165,42,42]
    elif HC=="White":
        HC=[255,255,255]
    elif HC=="Gray":
        HC=[128,128,128]
    elif HC=="Black":
        HC=[0,0,0]
    else:
        HC=[color_R,color_R,color_R]
    
    return HC

def  conv_FC(Favorite_color):
    FC=Favorite_color
    if FC=="Red":
        FC=[220,20,60]
    elif FC=="Pink":
        FC=[255,192,203]
    elif FC=="Orange":
        FC=[255,127,80]
    elif FC=="Gold":
        FC=[255,215,0]
    elif FC=="Purple":
        FC=[238,130,238]
    elif FC=="Green":
        FC=[50,205,50]
    elif FC=="Bule":
        FC=[135,206,235]
    elif FC=="Brown":
        FC=[165,42,42]
    elif FC=="White":
        FC=[255,255,255]
    elif FC=="Gray":
        FC=[128,128,128]
    elif FC=="Black":
        FC=[0,0,0]
    else:
        FC=[color_R,color_R,color_R]
    
    return FC