# Assume two values: value 1 and value2:
# Write set of sequence which prints a „True‟ if the value 1 is divisible by value 2 . Otherwise it should print a „False‟

valuel= int(input("Enter Value 1 \n"))
value2= int(input ("Enter Value 2 \n"))
print(valuel % value2 == 0, "\n")


# Write sequence of commands to convert and print a string in uppercase. 
# Write a string in reverse order 

string="This is a string"
print(string)
print(" Applying upper function  :\t", string.upper())
print(" Applying reverse function  :\t", string[::-1],"\n")


# name = "John"
# if name in ["John", "Rick"]: print("Your name is either John or Rick.")
# if name in ["kuber", "akshit"]: print("Your name is either John or Rick.")

name="Pratibha"
list1 =["Pratibha", "Pratuu"]
list2 =["music","earphone","phone"]
if name in list1: print ("My name is either", list1[0]," or ", list1[1])
if name in list2: print ("My name is either", list2[0], list2[1]," or ", list2[2])
 

#  Print a multiline string   
s= "\n this is a multiline string \n This is second assignment of Python in Cad Lab \n I am using backslash n for writing multiline string \n"
print(s)
