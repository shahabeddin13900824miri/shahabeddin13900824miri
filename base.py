# imports
import os
import hashlib
# check password
password = input('password: ')
enpassword = 'db28d9cebbe9b99a38b50046375161407f5c6a0fe29c0a5070b8bc4dcbb60946'
password = hashlib.sha256(password.encode())
password = password.hexdigest()
while password == enpassword:
    # filter some words
    do = input('say: ')
    if 'hello' in do:
        print('hi')
        do = do.replace('hello','')
    if 'hi' in do:
        print('hi')
        do = do.replace('hi','')
    if 'how are you' in do:
        print('im fine thank you. and you')
        do = do.replace('how are you', '')
    if 'please' in do:
        do = do.replace('please','')
    if 'im fine thank you' in do:
        do = do.replace('im fine thank you','')
    if 'open' in do:
        do = 'openApps'
    if 'bye' in do:
        do = do.replace('bye','')
        break
    # open some file to do works
    
    os. system('%s.py'%(do))