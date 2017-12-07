
#print ('This application is meant to provide.')

print('Please input a number.')

num = input()

num = int(num)

if num % 4 == 0:
    print (num, 'is a multiple of 4. Therefore it is even by definition.')
elif num % 2 == 0:
    myList = []
    for i in range(1, num + 1):
        if num % i == 0:
            myList.append(i)
    print (num, 'is an even number. Its factors are', myList,'.')
else:
    myList = []
    for i in range(1, num + 1):
        if num % i == 0:
            myList.append(i)
    print(num, 'is not an even number. Its factors are',myList,'.')
