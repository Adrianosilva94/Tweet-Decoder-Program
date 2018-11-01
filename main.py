'''
Name: Adriano Moreira
Email: adriano.moreira@owl.ucc.edu
Date: Thursday, November 1, 2018
Program description: This program was developed to decode abbreviations from tweeter. First the user inserts (input) a complete tweet with limit of 160 characters in a single line. If the input lengh is bigger than 160 characters, the program will display an error message. Next, the program analize the input and prints a list of abreviations found if any. Ultimately, the program prints a decoded version of the tweet inserted.

#Required inputs:
  #1 "lol cuz iirc I was afk I'll brb I have to go ttyl"
  #2 "I don't know man, I think you are going to get hired cuz iirc she said you did good with the interview. But do not worried man, if anything we will sell timeshares lol... ttyl bro brb"
#Expected outputs:  
  #1 laughing out loud because if i recall correctly i was away from keyboard i'll be right back i have to go talk to you later
  #2 Error! Only 160 characters allowed!

'''

abb = { 'lol': 'laughing out loud', 
        'bfn': 'bye for now',
        'ftw':'for the win',
        'irl':'in real life', 
        'cuz': 'because', 
        'afk': 'away from keyboard', 
        'nvm': 'never mind', 
        'iirc': 'if i recall correctly', 
        'ttyl': 'talk to you later', 
        'brb': 'be right back' }

print('WELCOME TO TWEET DECODER')
print()
tweet = input('Enter a complete tweet (160 characters or less) :\n').lower()
if len(tweet) < 160:
 tweet.split()
 print('\nList of abbreviations found')

 if 'lol' in tweet:
  print('\nLOL = laughing out loud:')

 if 'bfn' in tweet:
  print('\nBFN = bye for now')

 if 'ftw' in tweet:
  print('\nFTW = for the win')

 if 'irl' in tweet:
  print('\nIRL = in real life')

 if 'cuz' in tweet:
  print('\nCUZ = because')

 if 'afk' in tweet:
  print('\nAFK = away from keyboard')

 if 'nvm' in tweet:
  print('\nNVM = never mind')

 if 'iirc' in tweet:
  print('\nIIRC = if i recall correctly')

 if 'brb' in tweet:
  print('\nBRB = be right back')

 if 'ttyl' in tweet:
  print('\nTTYL = talk to you later')

else:
 print ("\nError! Only 160 characters allowed!")
 exit()
print()
print('Tweet decoded:')
print()
print(' '.join([abb.get(word,word) for word in tweet.split()]))
name = 'Adriano Moreira'
date = 'Thursday, November 1, 2018'
print('\n Programmed by %s on %s.' %(name,date))

