num1,num2,num3=int(input()),int(input()),int(input())
maior=menor=num1

if maior<num2:
    maior=num2
if maior<num3:
    maior=num3

if menor>num2:
    menor=num2
if menor>num3:
    menor=num3

intermediario=(num1+num2+num3)-(maior+menor)

print(intermediario)
