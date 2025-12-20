"""LOOPS"""

""" 
1.
name = "Piu"
for ch in name:
     print(ch)

   Output:
         P
         i
         u

"""


"""
2.
for i in range(1, 6):
           print(i)

    Output:
          1
          2
          3
          4
          5

"""


"""
3.
fruits = ["Apple", "Orange", "Cherry"]
for x in fruits:
    print(x)

    Output:
          Apple
          Orange
          Cherry

"""


"""
4.
fruits = ["cherry","Strawberry","banana","Mango"]
for x in fruits:
   print(x)
   if x == "banana":
      break
   
   Output:
         cherry
         Strawberry
         banana
"""


"""
5.
flowers = ["rose","sunflower","Lotus","Tulip"]
for x in flowers:
    if x == "Lotus":
        continue
    print(x)

 Output:
 rose
 sunflower
 Tulip

"""


"""
6. 

for i in range(6):
     print(i)
else:
     print("finally finished")

     Output:
            0
            1
            2
            3
            4
            5
            finally finished
"""


"""DATA STRUCTURE"""

"""
1.

list = ["apple","banana","orange","cherry"]
list.insert(1,"kiwi")
list.sort()
list.remove("banana")
list[1] = "strawberry"
list.extend(["banana","papaya","guava"])
print(list)

  Output:
           ['apple', 'strawberry', 'kiwi', 'orange', 'banana', 'papaya', 'guava']

"""


"""
2.
t1 = (10,20)
t2 = (30,40,50)
t3 = t1 + t2
print(t3)

Output: (10, 20, 30, 40, 50)

"""


"""
3.
set = {1,2,3,3,4,5}
print("set of numbers: ",set)
set.add(6)
set.update([7,8]) #add multiple items
print("After adding elements: ",set)
print("is 3 in the set", 3 in set)
set.remove(4) #  error if not present
set.discard(10)  # no error if not present
print("set is : ",set)

Output:
set of numbers:  {1, 2, 3, 4, 5}
After adding elements:  {1, 2, 3, 4, 5, 6, 7, 8}
is 3 in the set True
set is :  {1, 2, 3, 5, 6, 7, 8}

"""

"""
4. set operations

set_a = {1,2,3}
set_b = {3,4,5}
print("Union: ",set_a | set_b)
print("Intersection: ",set_a & set_b)
print("difference: ", set_a - set_b)

Output:
Union:  {1, 2, 3, 4, 5}
Intersection:  {3}
difference:  {1, 2}

"""

"""
5.

"""

dict = {
    "name":"Asha",
    "age": 18,
    "garde": "A"
}

print(dict)
print(dict["name"])
print(dict.get("age","not found"))

dict["age"] = 18
dict["garde"] = "A+"

print("Updated dictionary: ", dict)

dict.pop("age")
print("after removal: ",dict)

print("dictionary keys: ", dict.keys())
print("dictionary values: ",dict.values())
