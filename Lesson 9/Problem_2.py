#The code below imports a time package so that there is a delay during the processing string
import time

print('-' * 60)

print('I am Locker Bot: ')
print()
print()

password = input('Please input the password!: ')
if password == 'Open Sesame':
	
	print()
	print(' ... Processing ...')
	time.sleep(0.5)
	print(' ... Processing ...')
	time.sleep(0.5)
	print(' ... Processing ...')
	time.sleep(0.5)
	print()
	
	print('Password is valid! ')
	print('Locker opening! ')
else:
	

	print()

	print(' ... Processing ...')
	time.sleep(0.5)
	print(' ... Processing ...')
	time.sleep(0.5)
	print(' ... Processing ...')
	time.sleep(0.5)
	
	print()

	print('Password is invalid')
	print()
	print('You are now locked out. Have a nice day!')
print('-' * 60)
