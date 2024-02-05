import random
x = random.randint(1, 10)
y = int(input('Guess a number between 1 and 10:) - '))

if y == x :
  print('YOU GOT IT RIGHT!!!!! good job man1')
elif y not in [1,2,3,4,5,6,7,8,9,10] :
 print('ion think thats from 1 to 10 man')
else :
   while True :
    x = random.randint(1, 10)
    print('Aw, the number way', x )
    z =input('Care to try again?(y/n)')
    if z == 'y' :
       y = input('Guess a number between 1 and 10:) - ')
    else :
       print('thanks for playing:)') 
       exit()
  