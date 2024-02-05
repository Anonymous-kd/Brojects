class User() :
    def __init__(self, username, age, birthdate, password,) :
        self.username = username
        self.age = age
        self.birthdate = birthdate
        self.password = password
x =input('Hi there, welcome to *website Name*. Want to sign up? ')
if x == 'y' :
    print('**DISCLAIMER** make sure every input is accurate because it will be displayed on your profile.')
    username =input('ENTER YOUR FULL NAME: ')
    age =input("Enter AGE:") 
    birthdate =input('Enter your birthdate(dd/mm/yy): ')
    password =input('Enter your password: ')        
    p1 = User(username, age, birthdate, password)
    print(p1.password, 'Is your password, dont forget.')
    print('Welcome', p1.username, ', you are officially a member starting of today:)')
else :
    print('It seems like you dont want to sign up, thank you for your time.')
    exit()

print('Hi there, please login to your account:)')
x = input('enter your name: ')
y = input('Enter your password: ')

if x == username and y == password :
    print(p1.username, 'welcome to *websites name*')

else :
    print('Invalid Credentials.')    

