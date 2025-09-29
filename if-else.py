# n = int(input("Enter your Number? "))
# if (n % 2 == 0):
#     print("Even")
# else:
#     print("Odd")    

# n = int(input("Enter your Number? "))
# if (n > 0):
#     print("Postive")
# elif (n < 0):
#     print("Negative") 
# else:
#     print("Zero")       

# name = str(input("Enter your Name? "))
# age = int(input("Enter your Age? "))
# if (age >= 18):
#     print(f"{name} you are Eligible")
# else:
#     print(f"{name} you are not Eligible")
    
# n = int(input("Enter your Number? "))
# if (n % 3 == 0)  and (n % 7 == 0) or (n % 9 == 0):
#     print("Divisible")
# else:
#     print("Not Divisible")     
    
# amount = int(input("Enter the Amount of the Product? "))
# if amount > 100:
#     discount = int(amount * 0.1)
#     actual_price = int(amount - discount)
#     print(f"Discount price is {discount}")
#     print(f"Final price is {actual_price}")

# mark = int(input("Enter your Mark? "))
# if (mark >= 90):
#     print("\"A\" Grade")
# elif (mark >=80 and mark < 90):
#      print("\"B\" Grade")
# elif (mark >= 70 and mark < 80):
#      print("\"C\" Grade")
# elif (mark >= 60 and mark < 70):
#      print("\"D\" Grade")          
# else:
#     print("\"F\" Grade")      

# accountPin = 1234

# while True:
#     attempts = 3
#     for i in range(attempts):
#         pin = int(input("Enter your Pin: "))
#         if pin == accountPin:
#             amount = int(input("Enter your Withdrawal Amount: "))
#             if amount > 10000:
#                 print("Withdrawal Limit Exceeded")
#             else:
#                 print("Withdrawal Successful")
#                 exit()  # Exit the program after successful withdrawal
#         else:
#             print(f"Wrong Pin...only {2 - i} attempts left")
    
#     # If all attempts are used
#     print("Your Card is Blocked...Reset your Pin")
#     print("Change your Pin")
#     accountPin = int(input("Enter Your New Pin: "))

# username = "anshika28"
# password = "2802"
# user = input("Enter your Username? ")
# pswrd = input("Enter your Password? ")
# if (username == user) and (password == pswrd):
#     print("Login successful")
# else:
#     print("Wrong Credentials")

# n = int(input("Enter your Number? "))
# if (n >= 0):
#     print("Postive")
# else:
#     print("Negative") 

# n = int(input("Enter your Number? "))
# if (n % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# a = int(input("Enter a? "))
# b = int(input("Enter b? "))
# if (a > b):
#     print("\"a\" is the Largest Number")
# elif (b > a):
#       print("\"b\" is the Largest Number")  

# a = int(input("Enter a? "))
# b = int(input("Enter b? "))
# c = int(input("Enter c? "))
# if (a < b) and (a < c):
#     print("\"a\" is the Smallest Number")
# elif(b < c) and (b < a):
#      print("\"b\" is the Smallest Number")  
# elif(c < a) and (c < b):
#    print("\"c\" is the Smallest Number")       

# year = int(input("Enter the Year? "))
# if (year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("It's a Leap Year")
#         else:
#             print("It's not a Leap Year")   
#     else:
#         print("It's a Leap Year")
# else:
#     print("It's not a Leap Year")  

# a = str(input("Enter a Character? "))   
# if a in ("a","e","i","o","u"):
#     print("It's a Vowel")  
# else:                 
#     print("It's a Consonant") 

# num = int(input("Enter num? "))
# if(num % 5 == 0) and ( num % 11 == 0):
#     print("It's Divisible") 
# else:    
#     print("Not Divisible")


# num =int(input("Enter a Number? "))
# a=0
# for i  in range (num):
#     if(i%num ==0):
#         a +=1
# if(a<=1):
#     print("Prime")
# else:
#     print("not prime")

# mark = int(input("Enter your Mark? "))
# if (mark >= 90):
#     print("\"A\" Grade")
# elif (mark >=80 and mark < 90):
#      print("\"B\" Grade") 
# elif (mark >= 70 and mark < 80):
#      print("\"C\" Grade")
# elif (mark >= 60 and mark < 70):
#      print("\"D\" Grade")          
# else:
#     print("\"F\" Grade")

# ch = str(input("Enter a Character? ")) 
# if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
#     print("It's Alphabet")
# else:
#     print("It's not a Alphabet")    

# age = 18
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")    



# num = str(12321)
# reverse = num[::-1]
# if num == reverse:
#     print("Palindrome")
# else:
    # print("Not a Palindrome")
    
# num = int(123)    
# a = num
# newNum =0
# while(num>0):
#     digit = num % 10
#     print(digit)
#     newNum = newNum*10 +digit
#     print(newNum)
#     num = num//10
#     print(num)

# if(newNum== a):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# num = 8
# if(num >=0) and (num < 10):
#     print("Single-digit number")
# else:
#     print("Not a Single-digit number")    

# str = ""
# if len(str) == 0:
#     print("String is Empty")
# else:
#     print("String is not Empty")
    
# password = "mypassword"
# if len(password) >= 8:
#     print("Strong Password")
# else:
#     print("Weak Password")    

# import math
# n = 25
# sqrt_num = (math.sqrt(n))
# if sqrt_num == int(sqrt_num):
#     print("Perfect Square")
# else:
#     print("Not a perfect Square")    

# str1 = "hello"
# str2 = "worlds"
# s1 = len(str1)
# s2 = len(str2)
# if s1 > s2:
#     print("First string is longer")
# elif s2 > s1:
#     print("Second string is longer")    

# ch = "A"
# if ch.upper() == ch:
#     print("Uppercase")
# else:
#     print("Not a Uppercase")   

# temp = 105
# if temp >= 100:
#     print("Boiling")
# else:
#     print("Not Boiling")    

# marks = 45
# if marks >= 40:
#     print("Passed")
# else:
#     print("Not Passed")    

# str = "apple"
# if str[0].lower() in 'aeiou':
#     print("Yes")
# else:
#     print("No")    

# num = 64
# if (num % 2 == 0) and (num < 100):
#     print("Yes")
# else:
#     print("No")    

# income = 40000
# age = 25
# if (income > 30000) and (age > 21):
#     print("Eligible")
# else:
#     print("Not Eligile")    

# year = 1900
# if (year % 100 == 0):
#     print("Century")
# else:
#     print("Not a Century")    

# num = 7
# if (num % 2 == 0) and (num % 3 == 0):
#     print("Divisible by 2 and 3") 
# elif (num % 2 == 0):
#     print("Divisible by 2")
# elif (num % 3 == 0):
#     print("Divisible by 3")
# else:
#     print("Not Divisible by 2 and 3")       

# list = []   
# if len(list) == 0:
#     print("List is Empty")
# else:
#     print("List is not Empty")    

# word = "banana"
# if 'a' in word:
#     print("Yes")
# else:
#     print("No")    

# role = "admin"
# if role == "admin":
#     print("Access granted")
# else:
#     print("Access denied")    
     
# a = 60
# b = 60
# c = 60
# if (a+b+c) == 180:
#     print("Valid Triangle")
# else:
#     print("Not Valid Traingle")    

# a = 5
# b = 6
# c = 15
# if (a+b > c) and (b+c > a) and (c+a > b):
#     if (a == b) and (b == c) and (c == a):
#         print("Equilateral")
#     elif (a == b) or (b == c) or (c == a):
#         print("Isoceles")
#     else:
#         print("Scalene")    
# else:
#     print("Not valid Triangle")

# day = "Sunday"
# if day in ["Saturday","Sunday"] :
#     print("Weekend")
# else:
#     print("Week Day")    

# int = "10"
# if int.isdigit:
#     print("Integer")
# else:
#     print("Not a Integer")    

# x = 5
# y = 3
# if  x > 0 and y > 0:
#     print("First Quadrant")
# else:
#     print("Not")    

# str = 'notes.txt'
# if str.endswith('.txt'):
#     print("Text File")
# else:
#     print("Not Text File")   
 
# num = 8
# if num > 0:
#     while num % 2 == 0:
#         num = num // 2
#     if num == 1:
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("No")                

# letters = "abc"
# if letters.isalpha():
#     print("Alpabetic")
# else:
#     print("Numeric")    

# list = [1,2,2,3]
# if len(set(list)) != len(list):
#     print("Has Duplicates")
# else:
#     print("Original")    

# num = 153
# original = num
# sum_of_cubes = 0
# while num > 0:
#     digit = num % 10
#     sum_of_cubes += digit ** 3
#     num //= 10
# if sum_of_cubes == original:
#     print("Armstrong Number")    
# else:
#     print("Not a Armstrong Number")    
    
# email = "abc@example.com"
# if "@" in email:
#     print("Valid")
# else:
#     print("Not Valid")    

# tasks = [
#     "Complete Python coding assignment",
#     "Read 20 pages of a book",
#     "Workout for 30 minutes",
#     "Prepare healthy lunch",
#     "Call a friend",
#     "Revise interview questions"
# ]

# completed, incomplete = [], []

# for task in tasks:
#     if input(f"Did you complete '{task}'? (y/n): ").lower() == "y":
#         completed.append(task)
#     else:
#         incomplete.append(task)

# print("Completed:", completed)
# print("Incomplete:", incomplete)
# print(f"Summary: {len(completed)}/{len(tasks)} tasks completed")


tasks = [ ]
print(input("Day Started please plan your day! "))
n =  int(input("Enter the no of task for the day? "))
for i in range(n):
    task = input("Enter task? ")
    tasks.append(task)
completed_task = []
incompleted_task = []  
print(input("End of the day reviewed task! "))
for i in tasks:
    status = input(f"Did you completed the {i} task (Yes or No)?")
    if status.lower() == "Yes":
        completed_task.append(i)   
    else:
        incompleted_task.append(i)    
print(f"Completed Tasks are {completed_task}")
print(f"Incompleted Tasks are {incompleted_task}")
