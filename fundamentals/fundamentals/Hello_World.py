#------- Part 1 -----------

# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "Hello" , name )	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello", (name))	# with a comma
print( "Hello " + name)	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat", fave_food1, "and", fave_food2 ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food1}" ) # with an f string

#------- Part 2 -----------


print ("Hello World")
name = "Nader"
print ("Hello" , name , "!")
print ("Hello " + name + " !")
num = 7 
print ("Hello" , num, "!")
print ("Hello " + str(num) + " !")

favorite_food = ["pizza", "Sushi"]
print("I love to eat", favorite_food[0], "and", favorite_food[1])

# F String

print(f"I love to eat {favorite_food[0]} and {favorite_food[1]}")
