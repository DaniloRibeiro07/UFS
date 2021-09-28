num1=float(input())
op='A'
while op!='&':
    num2=float(input())
    op=input()
    try:
        if op=='+':
            num1=num1+num2
            print('%.3f'%num1)
        elif op=='*':
            num1=num1*num2
            print('%.3f'%num1)
        elif op=='/':
            num1=num1/num2
            print('%.3f'%num1)
        elif op=='-':
            num1=num1-num2
            print('%.3f'%num1)
    except:
        print("operacao nao pode ser realizada")