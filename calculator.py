num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
 

#  addition

if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
   
 #subtraction
 
elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
 
 #multiplication
 
elif choice == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
 
#  division

elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
 
else:
    print('Enter a valid operator, please run the program again.')
