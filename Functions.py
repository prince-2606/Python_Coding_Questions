# def painter():
#     print("Painting")
# painter()    

# def add():
#     print("Addition")
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     print(a+b)
# add()

# def sub(a,b):
#     print("Subraction")
#     print(a-b)
# sub(24,12) 

# def mul(a,b):
#     print("Multiplication")
#     print(a*b)
# mul(9,5)    

# def div(a,b):
#     print("Division")
#     print(a/b)
# div(49,5)   

# def findevenorodd(num):
#      if num % 2 == 0:
#          print("Even")
#      else:
#          print("Odd") 
# findevenorodd(999)          

# def findpassorfail(mark):
#     if(mark >= 35):
#         print("Pass")
#     else:
#         print("Fail") 
# findpassorfail(100)

# def printrange(a,b):
#     for i in range(a,b):
#      print(i) 
# printrange(0,100)       

# username = "Prince" 
# password = "2606" 
# u_name = input("Enter your Username? ")
# p_word = input("Enter your Password? ") 

# def validate():
#     # username = "Prince" 
#     # password = "2606"
#     # u_name = input("Enter your Username? ")
#     # p_word = input("Enter your Password? ") 
#     if (username == u_name and password == p_word):
#      return True
#     else:
#         return False
   
   
# def add(a,b,c):
#     return (a+b)*c
# print(add(25,25,25))

# def square_of_number(n):
#     print(n*n)
# square_of_number(4)    

# def square_of_number(n):
#     return n*n
# print(square_of_number(4))  

# def even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# print(even(10))    

# def Factorial(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial *= i
#     return factorial
# print(Factorial(5))      

# def Maximum(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > a and c > b:
#         return c
# print(Maximum(10,20,15))

# def Palindrome(str):
#     reverse = str[::-1]
#     if str == reverse:
#         return True
#     else:
#         False
# print(Palindrome("madam"))        

# def Vowels(str="education"):
#     count = 0
#     for i in str:
#         if i in "aeiou":
#             count += 1
#     return count    
# print(Vowels())  

# def reverse_list(num):
#     reverse = num[::-1]
#     return reverse
# print(reverse_list([1,2,3]))


# def Sum(num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum
# print(Sum([1,2,3,4]))    

# def prime(n):
#     count  = 0
#     for i in range(1,n):
#         if n % i == 0:
#             count += 1
#     if count <= 1:
#         return True
#     else:
#         return False
# print(prime(7))       

# def Fibonacci(num):
#     list =[]
#     a, b = 0, 1
#     for i in range(1, num+1):
#         list.append(a)
#         a, b = b, a + b
#     return list
# print(Fibonacci(5)) 

# def Area(r):
#     pi = 3.1416
#     area = pi * (r**2)
#     print(round(area,2))
# Area(5)    

# def Convert(C):
#     F = (C * 9/5) + 32
#     return F
# print(Convert(0))    

# def Sum(num):
#     # num = str(num)
#     sum = 0
#     for i in str(num):
#         sum += int(i)
#     return sum 
# print(Sum(1234))    

# def Length(str):
#     return(len(str)) 
# print(Length("hello"))    
        
# def Minimun(list):
#     n = list[0]
#     for i in list:
#         if(n<i):
#             n=i
#     return min(list)
# print(Minimun([4,2,9,1]))     
            
# def perfectNumber(num):
#     sum =0
#     for i in range(1,num):
#         if num % i == 0:
#            sum += i
#     if(num == sum):
#         return True
#     else:
#         return False
# print(perfectNumber(28))

# def numberOf(words):
#     split1 = words.split()
#     return len(split1)
# print(numberOf("This is a test"))

# def Count(str1):
#     count = 0
#     for char in str1:
#         if char.isupper():
#             count += 1
#     return count   
# print(Count("Hello World"))        
    
def evenNumber(n):
    even = []
    for i in n:
        if (i % 2 == 0):
            even.append(i)    
    return even
print(evenNumber([1,2,3,4,5]))    

def secondlargest(n):
    lst mn   = [] 
    