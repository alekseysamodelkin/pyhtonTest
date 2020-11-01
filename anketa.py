# -----------------------------
# Program by Samodelkin
# -----------------------------
print('What\'s your name?')
name = input()
print("Nice to meet you, ", name, '!', sep='')
age = int(input('How old are you, ' + name + '?'))
print("I have thought you are - ", age+1, end='')
x = age+1
if x >=13 and x<=19:
    print(", teen!")
else:
    print(", old")
