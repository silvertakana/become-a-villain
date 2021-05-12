import random
id = round(random.random() * 8999 + 1000)
name = input("your name: ")
print("hello ("+name+"), welcome to the Cyber Villain Association")
print("call it CVA for short")
print("now please enter your age")
age = input("age: ")

# print(id)
if int(age) < 17:
    print("you are "+age+"? pfft you are too young go home kid")
else:
    print("congrats you are now officially a member of CVA.")

    print("we will call you "+name+age+"#"+str(id))
