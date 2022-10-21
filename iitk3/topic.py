# greetings="hi"
# name="akanshu"
# end="how are you"
# print(greetings,end="")
# print(name,end="\n")
# print(end)
# num=int(input("enter your number:"))
# a=62
# b=12
# print(type(a))
# print(type(b))
# print(a+b)
# print(a*b)
# print(a**b)
# print(a/b)
# print(a//b)
# print(a>b)
# print(a<b)
# print(a==b)
# print(a%b)
# question
# money=82
# item=60
# choclate=20
# if(money-item>choclate):
#     if(money-item>2*choclate):
#         print("you can buy 2 choclates also")
#     elif(money-item>23):
#         print("you are low on money")
#     else:
#         print("you can't buy choclate")
# else:
#     print("sorry you cant buy choclates")
# num=(int(input("enter your number:")))
# if(num%2==0):
#     print("num is even")
# else:
#     print("num is odd")
#question
# n=int(input("enetr your no:"))
# if(n%2==0):
#     if(2<n<5):
#         print("not weird")
#     elif(6<n<20):
#         print("weird")
#     elif(n>20):
#         print("not weired")
# else:
#     print("weired")
# for x in "banana":
#     print(x)
# for i in range(1,10,3):
#     print(i)
# print(" ")
# sum=10
# for i in range(6):
#     sum+=i
# print(sum)
# sum=0
# n=int(input("enter your no :"))
# for i in range(n+1):
#     sum+=i
# print(sum)
# sum=0
# i=0
# while(i<=5):
#     sum+=i
#     i+=2
# print(sum)
# sum=0
# i=0
# n=int(input("enter your number:"))
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)
# sum=0
# i=0
# while(i<=3):
#     sum+=i*i*i
#     i+=1
# print(sum)
# sum=0
# for i in range (4):
#     cube=i**3
#     sum+=cube
# print(sum)
# sum=0
# i=0
# n=int(input("enter your no:"))
# while(i<=n):
#     sum+=i**3
#     i+=1
# print(sum)
# sum=0
# n=int(input("enter your no :"))
# for i in range (0,n+1):
#     cube=i**3
#     sum+=cube
# print(sum)
# sum=0
# i=0
# n=int(input("enter your no:"))
# while(i<=n):
#     sum+=i**2
#     i+=1
# print(sum)
# for i in range(1,10):
#     if(i==7):
#         break
#     print(i)
# i=0
# while(i<=8):
#     if(i==5):
#         break
#     i+=1
#     print(i)
# for i in range(1,10):
#     if(i==7):
#         continue
#     print(i)
# i=0
# while(i<=10):
#     i+=1
#     if(i==6):
#         continue
#     print(i)
# for i in range(1,10):
#     if(i==5 or i==7):
#         continue
#     print(i)
# i=0
# while(i<=10):
#     i+=1
#     if(i==4 or i==7):
#         continue
#     print(i)
# i=2
# while(i<=10):
#     i+=1
#     if(i==2 and i== 3):
#         continue
#     print(i)
# for i in range(1,5):
#     for j in range(1,5):
#         print(i+j,end=" ")
sum=0
n=int(input("enter your number:"))
for i in range (0,n+1):
    sum+=i
    print(sum/n)