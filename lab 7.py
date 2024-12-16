# 7 in a string find uppercase and lower case letter:
user=input()
lower=0
upper=0
for i in user:
    if  i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(f"Number of Lower letter: {lower}")
print(f"Number of Upper letters: {upper}")
