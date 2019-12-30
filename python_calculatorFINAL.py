NUM1 = int(input('ENTER A NUMBER: '))
OP = input('ENTER AN OPERATOR: ')
NUM2 = int(input('ENTER A NUMBER: '))

if OP == '+':
    print(NUM1 + NUM2)
elif OP == '-':
    print(NUM1 - NUM2)
elif OP == '/':
    print(NUM1 / NUM2)
elif OP == '//':
    print(NUM1 // NUM2)
elif OP == '%':
    print(NUM1 % NUM2)
elif OP == '*':
    print(NUM1*NUM2)

elif OP == '**':
    print(NUM1**NUM2)

else:
        print('INVALID OPERATOR ERROR')


        #Here is a list of operators you can enter
               # +, -, //, /, %, *, and **
            #THIS IS STILL A WORK IN PROGRESS
