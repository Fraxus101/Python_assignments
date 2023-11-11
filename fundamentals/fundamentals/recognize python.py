num1 = 42 #variable declaration, Initialize interger
num2 = 2.3 #variable declaration, initialize float
boolean = True #Boolean
string = 'Hello World' #variable declaration, Initialize Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #type check 
print(pizza_toppings[1]) #log statement : Prints the second value in the list "pizza_toppings" which is "Sausage"
pizza_toppings.append('Mushrooms') # add value : adds another value at the end of the list "pizza_toppings"
print(person['name']) #log statement
person['name'] = 'George' #change value : changes the value 'John' to 'George'
person['eye_color'] = 'blue' #IndexError: list index out of range : 'eye_color' does exist in the dictionary 'person'
print(fruit[2]) : #log statement : prints the third value in the tuple 'fruit' and shows 'banana'

if num1 > 45: #conditional, if
    print("It's greater") #log statement
else: #conditional, else
    print("It's lower") #log statement

if len(string) < 5: #conditional if, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if 'elif', length check
    print("It's a long word!") #log statement
else: #conditional, else
    print("Just right!") #log statement

for x in range(5):  #for loop
    print(x) #log statement
for x in range(2,5):  #for loop, start (2), stop (5)
    print(x) #log statement
for x in range(2,10,3): #for loop, start (2), stop (10), increment (3)
    print(x) #log statement
x = 0 #variable declaration, integer
while(x < 5): #while loop
    print(x) #log statement
    x += 1 #change value

pizza_toppings.pop() #delete last value
pizza_toppings.pop(1) #delete second value in the list

print(person) #log statement
person.pop('eye_color') #IndexError: list index out of range : 'eye_color' does exist in the dictionary 'person'
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional, if
        continue #continue, if the topping == pepperoni, pepperoni will be skipped 
    print('After 1st if statement')  #log statement
    if topping == 'Olives': #conditional, if 
        break #break, when the loop reaches the value 'Olives', the code will break and stops funtioning

def print_hello_ten_times(): #function
    for num in range(10): #for loop
        print('Hello') #log statement

print_hello_ten_times() #log statement

def print_hello_x_times(x): #function, parameter (x)
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4) #log statement, parameter (4)

def print_hello_x_or_ten_times(x = 10): #function, parameter (x = 10)
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #log statement, function
print_hello_x_or_ten_times(4) #log statement, funtion, parameter (4)


"""
Bonus section
"""

# print(num3) #comment, #log statement
# num3 = 72 #comment, #variable declaration, initialize integer
# fruit[0] = 'cranberry' #comment, change value
# print(person['favorite_team']) #comment, error
# print(pizza_toppings[7]) #comment, log statement, 
#   print(boolean) #comment, log statement, 
# fruit.append('raspberry') #comment, remove value
# fruit.pop(1) #comment, remove value