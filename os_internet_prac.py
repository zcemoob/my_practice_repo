import os

print("cwd is: " + os.getcwd())  # gives current folder

# comp1 = [2 ** x for x in range(10)]
# print(comp1)
# print(type(comp1))

# comp_test = "".join([letter for letter in "Eric Idle" if letter.lower() not in 'aeiou'])
# print(comp_test)
# print(type(comp_test))

# [print(x) for x in os.listdir(os.getcwd()) if ".txt" in x] # not working?
[x for x in os.listdir(os.getcwd()) if ".py" in x]
print("listdir: " + str([x for x in os.listdir(os.getcwd()) if ".py" in x])) # had to convert to str (can't concatenate str to list)

print(os.path.dirname(os.getcwd()))  # gives parent folder of current folder