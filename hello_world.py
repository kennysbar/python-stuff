# ask the users name
name = input("What is you name?: ")
your_name = "your name is "
print(your_name + name)
# ask user for age
age = input("what is your age?: ")
print(age)
# ask user for city
city = input("where are you from?: ")
print(city)
# ask user what they enjoy
love = input("what do you love?: ")
print(love)
# create output text
string = "Your name is {} and you are {} years old. You ilve in {} and you love {}"
output = string.format(name, age, city, love)
# print output to screen

print(output)
