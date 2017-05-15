from sys import argv

script, filename = argv
#Asigns the file contents to txt
txt = open(filename)

print("Here's your file %r:" % filename)
#To read a file it needs the .read() method or
#it will just print info about the file
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
