#Learn python, dont skid my project :)
import requests
import os
import random
import string
import json
import sys
import argparse
import concurrent.futures
import NicksLibary as nick
from colorama import init
from colorama import Fore, Style
from tqdm import tqdm
from pystyle import Colors, Colorate
from pystyle import Center

nick.settitle(' Escape - Stxnd ')

init()

print(Center.XCenter(Colorate.Horizontal(Colors.blue_to_red, """
       
                                            ███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗
                                            ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
                                            █████╗  ███████╗██║     ███████║██████╔╝█████╗  
                                            ██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝  
                                            ███████╗███████║╚██████╗██║  ██║██║     ███████╗
                                            ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝
 
                                                          Made by Stxnd 
                                                     https://cracked.io/stxnd                                                                                                                                 

""")))

file = input(Colorate.Horizontal(Colors.blue_to_red, """File Name : """))

counter = 0
kek = 0

try:
    print(Colorate.Horizontal(Colors.blue_to_red, ' '))
    num_lines = sum(1 for line in open('mails.txt'))
    print(Colorate.Horizontal(Colors.blue_to_red,'\nGot {} Mails !'.format(num_lines)))

    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(2048))
    email_domains = ['gmail.', 'yahoo.', 'hotmail.', 'yahoo.', 'outlook.', 'laposte.', 'orange.', 'icloud',
                     'protonmail.', 'fastmail.', 'rambler.', 'mail.', 'hushmail.', 'wanadoo.']

    domain_end = ['com','ru','net','fr','ca','be']

    names = json.loads(open('mails.txt', encoding="utf8").read())
    surnames = json.loads(open('mails.txt', encoding="utf8").read())
    passwordlist = json.loads(open('password.txt', encoding="utf8").read())

except FileNotFoundError:
    print(Colorate.Horizontal(Colors.blue_to_red,'You are missing the Following Files: mails.txt, password.txt'))

def maincombo():
    global counter
    name = random.choice(names).lower() + random.choice(surnames).lower()
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))
    email_domain = random.choice(email_domains) + random.choice(domain_end)
    email = name + name_extra + '@' + email_domain
    password = random.choice(passwordlist)
    combo = ('{0}:{1}'.format(email, password)).encode()
    counter = (counter + 1)
    return combo

def mainmail():
    global counter
    name = random.choice(names).lower() + random.choice(surnames).lower()
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))
    email_domain = random.choice(email_domains) + random.choice(domain_end)
    email = name + name_extra + '@' + email_domain
    combo = ('{0}'.format(email)).encode()
    counter = (counter + 1)
    return combo

def writecombo():
    with open(file, 'ab') as f:
            combo = maincombo() + '\n'.encode()
            f.write(combo)
            f.close()

def writemail():
    with open(file, 'ab') as f:
            combo = mainmail() + '\n'.encode()
            f.write(combo)
            f.close()

def generatecombo():
    global kek
    while True:
        kek = (kek + 1)
        print(Colorate.Horizontal(Colors.blue_to_red,'Generating Wave: {}'.format(kek)))
        for counter in tqdm(range(10000), unit='Combos'):
            writecombo()
            
def generateemail():
    global kek
    while True:
        kek = (kek + 1)
        print(Colorate.Horizontal(Colors.blue_to_red,'Generating Wave: {}'.format(kek)))
        for counter in tqdm(range(10000), unit='Combos'):
            writemail()

with concurrent.futures.ProcessPoolExecutor() as executor:
    print(Colorate.Horizontal(Colors.blue_to_red,'\nAvaiable modes: standard(email:pass), email(email)'))
    argument = input(Colorate.Horizontal(Colors.blue_to_red,'\nMode: '))
    if argument == 'email':
        while True:
            generateemail()
    else:
        while True:
            generatecombo()
