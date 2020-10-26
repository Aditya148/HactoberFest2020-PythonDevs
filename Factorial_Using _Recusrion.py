#Function to calculate factorial of the input number 
def fact(n): 
    #Using Recursion 
    return 1 if (n==1 or n==0) else n * fact(n - 1);  

#Taking input
num = int(input('Enter the number to find the factorial: ')); 
print('Factorial of {} is: {}'.format(num, factorial(num)))
