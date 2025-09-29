# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end =" ")
#     print() 

#INCREASING TRIANGLE:
 
# *
# * *
# * * *
# * * * *
# * * * * *
# n = 5   
# for i in range(n):
#      for j in range(i+1):                                          8                 
#          print("*",end =" ")
#      print()    
    
#DECREASING TRIANGLE:

# * * * * *
# * * * *
# * * *
# * *
# *
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end =" ")
#     print()   
    
# RIGHT SIDED TRIANGLE  

#          *
#        * *
#      * * *
#    * * * * 
#  * * * * * 

# n = 5 
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end ="")
#     for k in range(i+1):
#         print("*",end ="")
#     print() 
  
  
# HILL PATTERN

#           *     
#         * * *          
#       * * * * *            
#     * * * * * * *             
#   * * * * * * * * *             
    
# n = 5
# for i in  range(n):
#     for j in range(i,n):
#         print(" ",end ="")
#     for k in range(i):
#         print("*",end ="")
#     for l in range(i+1):
#         print("*",end ="")   
#     print()
                   
# REVERSE HILL PATTERN

#  * * * * * * * * * 
#    * * * * * * *                 
#      * * * * *
#        * * *
#          *

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end ="")
#     for k in range(i,n-1):
#         print("*",end ="")
#     for l in range(i,n):
#         print("*",end ="")
#     print()    
    
# DIAMOND PATTERN
    
    
#           *     
#         * * *          
#       * * * * *            
#     * * * * * * *                
#   * * * * * * * * * 
#     * * * * * * *                 
#       * * * * *
#         * * *
#           *

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end ="")
#     for k in range(i):
#         print("*",end ="")
#     for l in range(i+1):
#         print("*",end ="")
#     print()    
# for i in range(n):    
#     for a in range(i+1):
#         print(" ",end ="")
#     for b in range(i,n-1):
#         print("*",end ="") 
#     for c in range(i,n):
#         print("*",end ="")          
#     print()

#PATTERN QUESTIONS

# n = 4
# for i in range(n):
#     for j in range(n):
#         print("*",end ="")
#     print()  
    
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end ="") 
#     print()    

# n = 5
# for i in range(n):
#     for j in range(i,n):
#          print("*",end ="") 
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end ="") 
#     for k in range(i+1):
#         print("*",end ="")         
#     print()  

# n = 5
# for i in range(n):
#     for j in range(i,n):
#          print(" ",end ="") 
#     for k in range(i):
#          print("*",end ="")  
#     for l in range(i+1):
#          print("*",end ="")             
#     print()    

# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end ="")
#     for k in range(i,n-1):
#         print("*",end ="")   
#     for l in range(i,n):
#         print("*",end ="") 
#     print()

# n =  5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end ="")
#     print()      
    
n =  5
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end ="")
        num += 1
    print() 


    