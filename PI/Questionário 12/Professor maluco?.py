def professor_desgracado(num):
    if num=='0':
        return ''
    else:
        return professor_desgracado(input())+num+'\n'
    
print(professor_desgracado(input()))