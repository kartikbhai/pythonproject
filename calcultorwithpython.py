opr1=eval(input('enter first operand:-'))
opr2=eval(input('enter second operand:-'))
oprand=input('choose operation [+,-,*,**,%,//,/]:-')
if oprand=='+':
   print(opr1+opr2)
elif oprand=='-':
   print(opr1-opr2)
elif oprand=='*':
   print(opr1*opr2)
elif oprand=='**':
   print(opr1**opr2)
elif oprand=='%':
   print(opr1%opr2)
elif oprand=='/':
   print(opr1/opr2)
elif oprand=='//':
    print(opr1//opr2)
else:
    print('enter a valid operator')



