import random
id = round(random.random() * 8999 + 1000)
name = input("your name: ")
print("hello "+name+", welcome to the Cyber Villain Association")
print("call it CVA for short")
print("now please enter your age")
year_of_birth = int(input("year of birth: "))
this_year = 2021
age = this_year - year_of_birth

# print(id)
if int(age) < 17:
    print("you are "+str(age)+"? pfft you are too young, go home kid")
else:
    print("you must be "+str(age)+" years old")
    print("congrats you are now officially a member of CVA.")
    print("your code name is "+name+str(age)+"#"+str(id))
