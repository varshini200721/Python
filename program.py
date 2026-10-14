1.check even or odd
n=2
if(n%2==0):
  print("even number")
else:
  print("odd nummber")
o/p
   even number

2.check positive,negative or zero
a=2
if(a>0):
 print("positive")
elif(a<o):
 print("negative")
else:
print("zero")
o/p
positive

3.find the largest of two numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if(a>b):
  print("A is largest")
else:
  print("B is largest")
o/p
enter first number:10
enter second number:20
B is largest

4.check voting eligibility
a=int(input("enter your voting:"))
if(a>=22):
  print("your voting is eligible")
else:
  print("your voting is eligible")
o/p
enter your voting:18
your voting is eligible

5.check pass or fail
a=int(input("enter your mark:"))
if(a>75):
  print("pass")
else:
  print("fail")
o/p
enter your mark:60
fail

6.find the largest of three numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b):
  print("A is largest")
elif(b>c):
  print("B is largest")
else:
  print("C is largest")
o/p
enter first number:50
enter second number:30
enter third number:40
A is largest

7.check leap year or not
a=int(input("enter a year:"))
if a%4==0:
  print("leap year")
else:
  print("not a leap year")
o/p
enter a year:2024
leap year

8.check whether a number is divisible by 5
a=int(input("enter a number:"))
if(a%5==0):
  print("divisible by 5")
else:
  print("not divisible by 5")
o/p
enter a number:20
divisible by 5

9.check whether a number is divisible bt 5 or 3
a=int(input("enter a number:"))
if(a%5==0) and (a%3==0):
  print("divisible by 5 or 3")
elif(a%5==0):
  print("divisible by 5")  
elif(a%3==0):
  print("divisible by 3")
else:
  print("not divisible by 5 or 3")
o/p
enter a number:12
divisible by 3

10.find smallest of three numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a<b):
  print("A is smallest")
elif(b<c):
  print("B is smallest")
else:
  print("C is smallest")
o/p
enter first number:2
enter second number:1
enter third number:3
B is smallest

11.check whether a number two digit number or not
n=int(input("enter a number"))
if(n>10) and (n<99):
  print("two digit number")
else:
  print("not a two digit number")
o/p
enter a number79
two digit number

12.check whether the last digit is 5
a=int(input("enter the number"))
if(a%5==):
  print("last digit is 5")
else:
  print("last digit is not 5")
o/p
enter the number15
last digit is not 5
13.check whether a character is upper case or lower case
a=str(input("enter a character:"))
if a.isupper():
  print("upper case")
else:
  print("lower case")
  o/p
  enter a character:a
lower case

14.check whether a character is an alphabet digit or special character
a=input("enter a value:")
if a.isalpha():
  print("alphabet")
elif a.isdigit():
  print("digit")
else:
  print("special character")
  o/p
  enter a value:#
special character
  
15.check whether a persons temperature is above below are equal to 37 degree c 
temp=int(input("enter a temperature:"))
if(temp>37):
  print("above")
elif(temp<37):
  print("below")
else:
  print("equal to temp")
  o/p
  enter a temperature:40
above

16.calculate a 10% discount of a shopping bille exit 2000
bill=int(input("enter shopping bill:"))
if(bill>2000):
  discount=bill*10/100
  bill=bill-discount
  print("final bill:",bill)
  o/p
  enter shopping bill:3000
final bill: 2700.0

17.check whether a student get a scholershipif mark are atleast 90 and attendence is atleast 85%
mark=int(input("ener a mark:"))
attendance=float(input("enter a attendance:"))
if(mark>=90) and (attendance>=85):
  print("eligible")
else:
  print("not eligible")
  o/p
  ener a mark:95
enter a attendance:87
eligible

18.count number divisible by 5
count=0
for i in range(1,51):
  if i%5==0:
    count+=1
print(count)    
o/p
10

19.find the sum of old number
sum=0
for i in range(1,21):
 if(i%2==0):
   sum+=i
print(sum)
o/p
110

20.print number divisible by 3 but not by 4
for i in range(1,31):
  if(i%3==0) and (i%4!=0):
    print(i) 
o/p
3
6
9
15
18
21
27
30

21.count positive and negative number
n=int(input("how many numbers?:"))
for i in range(n):
  n=int(input("enter a number:"))
  
  if n > 0:
    print("positive")
  elif n < 0:
    print("negative")
  else:
    print("zero")
    o/p
how many numbers?:2
enter a number:6
positive
enter a number:0
zero



