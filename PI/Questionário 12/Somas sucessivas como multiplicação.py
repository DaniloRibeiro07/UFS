def somas_sucessivas(num1,num2):
    if num2==0 or num1==0:
        return 0
    else:
        if(num2<0):
            return -somas_sucessivas(num1,-num2)
        else:
            return num1+somas_sucessivas(num1,num2-1)
        
print(somas_sucessivas(int(input()),int(input())))