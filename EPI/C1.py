#Chapter 2 Arrays
"""
<Questions>

Basic array operations

* check if value in array : 
* diff between A=B and A= list(B)
* deep copy vs copy
* binary search
* min,max
* slicing array 
* slicing array with three values
* use slicing to create copy
* list comphrehension basic
* list comphrehension , 2d list to 1d
* list comphrehension , create set
(avoid using more than two)
* list and array difference 
"""


"""
5/6/23
<Questions>

Basic array operations

* check if value in array :
> a in A

* list with mutable objects : 
> List of lists: A list of lists contains references to other list objects, which are themselves mutable. For example: [[1, 2], [3, 4], [5, 6]]
> List of dictionaries: A list of dictionaries contains references to dictionary objects, which are themselves mutable. For example: [{1: "one", 2: "two"}, {3: "three", 4: "four"}, {5: "five", 6: "six"}]
> List of sets: A list of sets contains references to set objects, which are themselves mutable. For example: [set([1, 2]), set([3, 4]), set([5, 6])]
> List of user-defined objects: A list can also contain references to user-defined objects that are themselves mutable. For example, if we define a Person class with mutable attributes like name and age, we can create a list of Person objects: [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 35)]

* diff between A=B and A= list(B)
> A =B assigns two names for the array [1,2,3] and A = list(B) creates a new copy of the array
> A=B takes O(1) time (just reference creation) while A=list(B) takes O(n) time creating a completely new copy 
> changing a value in A will result in a change in B regardless of being mutable or not mutable

> When you create a new list object with the same elements as an existing list using the list()
> function, the new list object contains references to the same mutable objects as the original list.
> This means that if you modify one of these mutable objects through one list, the change will be reflected in both lists, because both lists contain references to the same mutable object.

* diff between list(B) and copy.copy()
> list(B) creates a new objects with the same elements as B. but the mutable objects will have the same references
    > so if you mutate an list(B) mutable object, it will also change the original 
> copy.copy on the other hand also creates objects for mutable objects so changing the mutable object will not change the 
 

* deep copy vs copy
> !! if the lists contain mutable objects
> copy just creates a reference to that element in the array. B= copy.copy(A) , same memory location
> as original object. So even after you create copy if you modify A it will also modify B
> on the other hand the deep copy creates a completely new object
> creating 
> copy.copy takes 

* diff btw A=B and copy.copy()
> copy.copy() creates a shallow copy of an object, which means that it creates a
> new object with a different memory address that contains references to the same 
> objects as the original object. 
> A=B creates a new reference to the same object as B, A and B refer to the same object in memory.
> operations are quite similar, the concepts are what differ.

*** final coding plan
if nonmutable list , and you want one change to not be reflected in other , use A=list(B) or A = copy.copy(B),
    > copy.copy() and list() have same time complexity, list() just has no import statements
if mutable list, just use copy.deepcopy() 
    > O(nm) time, new object, and iteration, For example, if we have a list of n lists, and each sublist contains m elements, then the time complexity of copy.deepcopy() on this list would be O(n*m).


* binary search
* min,max
* slicing array 
* slicing array with three values
* use slicing to create copy
* list comphrehension basic
* list comphrehension , 2d list to 1d
* list comphrehension , create set
(avoid using more than two)
* list and array difference 
"""

# Coding Questions , comment 지우고 맞춰봐!

# A=B - list with nonmutable objects 
A = [1,2,3]
B = A 
B[0]=4
print(A) # [4,2,3]
print(B) # [4,2,3]


# A=B - list with mutable objects 
A = [1,2,[1,3]]
B = A 
B[0]=4
B[2][0]=4
print(A) # [4, 2, [4, 3]]
print(B) # [4, 2, [4, 3]]




# A= list(B) -nonmutable list
A = [1,2,3]
B = list(A) 
B[0]=4
print(A)  # A = [1,2,3]
print(B) # B = [4,2,3]


# A= list(B) -mutable list
print(' A= list(B) -mutable list')
A = [1,2,[1,3]]
B = list(A) 
B[0]=4
B[2][0]=4
print(A)  # A = [1,2,[4,3]]
print(B) # B = [4,2,[4,3]]

A[2][1]=4
print(A)  # A = [1,2,[4,4]]
print(B) # B = [4,2,[4,4]]


# A= copy.copy(B) - nonmutable list
print('copy.copy(B) - nonmutable list')
import copy
A = [1,2,3]
B = copy.copy(A)
B[0]=4
print(A)   # [1,2,3]
print(B)   # [4,2,3]


# A= copy.copy(B) - mutable list
print('copy.copy(B) - mutable list')
import copy
A = [1,2,[1,3]]
B = copy.copy(A)
B[0]=4
B[2][0]= 4
print(A)  # A = [1,2,[4,3]] , only changes for mutable values
print(B) # B = [4,2,[4,3]]

A[2][1]= 4
print(A)  # A = [1,2,[4,4]] , only changes for mutable values
print(B) # B = [4,2,[4,4]]