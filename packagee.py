from collections.abc import Iterable
from random import randint
from random import choice
from string import ascii_lowercase

def unic():
    a = randint(1,20)
    b = randint(10,20)
    c = randint(15,20)
    d = randint(5,20)
    e = randint(0,20)
    return a * b * c*  d * e

def email_fake():
    ema = ""
    for i in [1,2,3,4,5]:
        ema = ema + choice(ascii_lowercase)
    return ema+"@email.com"

def password_fake():
    ema = ""
    for i in range(8):
        ema = ema + choice(ascii_lowercase)
    return ema

def my_hash(string:str):
    x = 928387
    txt = []
    for i in string:
        # print(ord(i))
        i = str(ord(i)+ x)
        txt.append(i)
    return ",".join(txt)

def trans_my_hash(string:str):
    x = 928387
    txt = ''
    for i in string.split(','):
        i = int(i) - x
        i = chr(int(i))
        txt = txt+i
    return txt

# for test 
if __name__ == '__main__':
    print(my_hash())
    print(trans_my_hash())
