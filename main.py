"""
    for i in range(5):
            print("Hello World!!!!!")

"""

# name = "Piu"
# for ch in name:
#      print(ch)

# for i in range(1, 6):
#            print(i)

# fruits = ["Apple", "Orange", "Cherry"]
# for x in fruits:
#     print(x)

# for x in "Sakshi":
#     print(x)

# fruits = ["cherry","Strawberry","banana","Mango"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#        break

# flowers = ["rose","sunflower","Lotus","Tulip"]
# for x in flowers:
#      if x == "Lotus":
#          continue
#      print(x)
         
# for i in range(6):
#     print(i)
# else:
#     print("finally finished")


# list = ["apple", "banana","orange"]
# list.append("cherry")
# print(list)

# list = ["apple","banana","orange","cherry"]
# list.insert(1,"kiwi")
# list.sort()
# list.remove("banana")
# list[1] = "strawberry"
# list.extend(["banana","papaya","guava"])
# print(list)


# creating tuple
# t1 = (10,20)
# t2 = (30,40,50)
# t3 = t1 + t2
# print(t3)

# t = (10,20,30,40,50)
# if 20  in t:
#     print("element found")


# def greet():
#     print("Hello World")

# greet()
'''
def stud_info(name= "", branch = "IT", college= "GPP"):
    print(name, branch, college)
stud_info("Sakshi") 
stud_info("Piu")
stud_info("Ashu") '''


# def emp(id="", name="",salary=""):
#     print(id,name, salary)
# emp(1,"sakshi",20000)
# emp(2,"Ashu","15000")
# emp(3,"Piu",30000)
# def marks(*marks):
#     return sum(marks)
# print(marks(10,20,30))


# def calculate(data):
#     return sum(data), sum(data)/len(data),max(data)
# s,avg,max = calculate([10,20,30])
# print(s,avg,max)
    

# def detail(**details):
#     print(details)
# detail(name= "Sakshi",age ="18",branch="IT")

# num = [10,20,30]
# print(*num)


#function with parameters
# def greet(name):
#     print("Hello", name)
# greet("Sakshi")


#function with return value

# def add(a, b):
#     return a +b 
# result = add(5,6)
# print(result)


# def add(a,b):
#     return(a + b)
# def sub(a, b):
#     return (a-b)
# def mul(a,b):
#     return(a * b)
# def div(a, b):
#     return(a/b)

# print(add(20,20))

# def sqr(num):
#     return num*num
# print(sqr(5))
    

# def sqr(num):
#     return num* num

# number = int(input("Enter number: "))
# result = sqr(number)
# print("Square of given number is : ",result)

# num = int(input("Enter number: "))
# sqr = num*num
# print("Square of ",num,"is",sqr)                                                                    

# def func(num):
#     if num % 2 ==0:
#         return "even"
#     else:
#         return "odd"

# number = int(input("Enter number: "))
# print(number,"is",func(number))

# def grade(marks):
#     if marks >= 90:
#         return "Grade A"
#     elif marks >= 75:
#         return "Grade B"
#     elif marks >= 50:
#         return "Grade C"
#     else:
#         return "Fail"
    
# student = int(input("Enter percentage: "))
# print(grade(student))

# def num_check(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else:
#         return "Zero"
    
# number = int(input("Enter number to check: "))
# print(number,"is",num_check(number))
 


# def large_num(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
    
# x = int(input("Enter first : "))
# y = int(input("Enter second: "))
# z = int(input("Enter third: "))

# print("Largest number is",large_num(x,y,z))


# def even_odd(lst):
#     for num in lst:
#        if num % 2 ==0:
#           print(num,"is Even")
#        else:
#           print(num,"is Odd")
    
# numbers = [1,2,3,4,5]
# even_odd(numbers)

# def check_year(year):
#     if year % 4 == 0:
#         return "Leap year"
#     else:
#         return "not a leap year"
    
# y  = int(input("Enter year to check: "))
# print(y,"is",check_year(y))

    
# import math_ex

# print(math_ex.add(10,20))
# print(math_ex.sub(20,5))
# print(math_ex.square(5))
# print(math_ex.pie)


# simple menu driven program
# while True:
#      print("\n******menu driven program******")
#      print("1. Add")
#      print("2. Sub")
#      print("3. Multiply")
#      print("4. divide")
#      print("5. Exit")

#      choice = input("Enter your choice(1-5): ")

#      if choice == '5':
#           print("Exiting the program")
#           break
     
#      elif choice in ('1','2','3','4','5'):     
#       num1 = float(input("Enter First number : "))
#       num2 = float(input("Enter second number: "))

#       if choice == '1':
#         print("Result: ",num1+num2)

#       elif choice == '2':
#         print("Result: ",num1-num2)

#       elif choice == '3':
#         print("Result: ",num1*num2)

#       elif choice == '4':
#          if num2 != 0:
#              print("Result: ",num1/num2)
#          else:
#           print("Cannot divide by Zero")

#       else:
#          print("Invalid choice please enter (1-5)")
          
     

# def check_max(a ,b):
#     if a > b:
#         return "a is greater"
#     elif b > a:
#         return "b is greater"
#     else:
#         return "both numbers are equal"

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))


# print(check_max(num1,num2))

# def interest(p ,r, t):
#     si = ( p * r * t)  /100
#     return si

# print(interest(10,20,30))

# def sum(n):
#     total = 0
#     for i in range (1,n+1):
#         total += i
#     return total

# print(sum(5))


# def math(a,b):
#     return a + b , a - b, a * b, a / b 

# add,sub,mul,div = math(4,2)
# print(add, sub, mul,div)


def typeprint(value):
    print("Value: ",value)
    print("Type: ",type(value))

    # typeprint(10)
    # typeprint(2.0)
    # typeprint("Sakshi")
    # typeprint(True)

value = input("Enter value to get type: ")
typeprint(value)
    