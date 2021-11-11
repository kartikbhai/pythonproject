k=0
j=0
email=input('enter your email:-')
a=len(email)
if a>=6:
    if email[0].isalpha() :
        if ('@' in email) and (email.count('@')==1):
            if (email[-1]=='m') and (email[-2]=='o') and (email[-3]=='c') and (email[-4]=='.'):
                for b in email:
                    if b!=' ':
                        k=1
                        # if b==b.lower():
                        #     j=b
                        # else:
                        #     print('problem in space or upper')
                            
                    else:
                        print('error in 5')
                if(k==1):
                    print('right email')
                else:
                    print('wrong email')
                        
            else:
                print('error in 4')
        else:
            print('error in 3')
    else:
        print('error in 2')

else:
    print('incorrect error 1')