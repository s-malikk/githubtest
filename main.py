
import random

name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))

print(name1 + " is " + str(age1) + " years old")

name2 = input("Enter your siblings name: ")
age2 = int(input("Enter your siblings age: "))

print(name2 + " is " + str(age2) + " yrs old")

ageDiff = age1 - age2

if ageDiff < 0:
    ageDiff = (ageDiff * -1)

if age1 > age2:
    print(name1 + " is " + str(ageDiff) + " years older than " + name2)
else:
    print(name2 + " is " + str(ageDiff) + " years older than " + name1)


we = random.randint(1, 10)
print("\n" + "The random integer is: " + str(we))
woo = int(input("Enter a num: "))
add = we + woo
print("Sum of numbers is: " + str(add))

rep = int(0)

for i in range(10):
    rep = rep + 1

print("\n" + str(rep))

#Given a string, identify the longest sequence of identical characters

word = input("\n" + "Enter a word: ")
length = len(word)
x = 0
omg = []
for i in range(length):
    omg.append(word[x])
    x = x + 1

print(omg)
