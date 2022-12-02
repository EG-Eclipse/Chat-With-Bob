print('Hello Friend! Whats your name?')
Name=input('Name: ')
print('Hello', Name, ' What would you like to call me?')
CompName=input('Whats my name: ')
print('[Input] Yes or No')
Sure=input(CompName, 'Are you sure:')
if(Sure.__contains__('Yes')):
  print('Alright, sounds good')
elif(Sure.__contains__('No')):
  print()
  app.stop()
print('What is your favorite number?')
Number=input('Number: ')
print('I like', Number, 'Too!')
print('What do you think about math?')
print('[Input] If you like math, input 1. If not, input 2.')
Math=input('Math: ')
if(Math.__contains__('1')):
  print('Good for you! Im not good at math.')
if(Math.__contains__('2')):
  print('Same here! Im just not good at math XD.')