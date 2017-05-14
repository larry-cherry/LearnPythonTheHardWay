x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Interpulates two types of variable string contents into the existing string
y = "Those who know %s and those who %s." % (binary, do_not)
#prints variable x
print(x)
#prints variable y 
print(y)

#prints string with x interpulated into it
print("I said %r." % x)
#prints string with y interuplated into it
print("I also said: '%s'." % y)
#asigns the variable with a boolean value
hilarious = False
#variable asigned to a string with a variable interpulation
joke_evaluation = "Is'nt that joke so funny?! %r"
#prints a variable and adds the second variable as an interpulation into the first
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
#concats two string together
print(w + e)