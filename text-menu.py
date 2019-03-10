#!/usr/bin/python

print (30 * '-')
print ("     menu")
print (30 * '-')
print ("1	==	configure server")
print ("2	== 	restart server")
print ("3	== 	something else")
print ("exit 	==  	reboot server")
print (30 * '-')


while True:

	choice = raw_input('Enter: ')
	 
	if choice == '1':
		print ("choice 1")
	elif choice == '2':
		print ("choice 2")
	elif choice == '3':
		print ("choice 3")
	elif choice == 'exit':
		break
	else:
		print ("wrong number")
