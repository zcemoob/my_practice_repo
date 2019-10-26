import json

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relationships": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relationships": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relationships": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relationships": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}
print(type(my_group))

# converts file into JSON string
file_as_string = json.dumps(my_group, indent=4)

# write data in a file called my_file.json
with open('my_file.json', 'w') as dest:
    dest.write(file_as_string)

# opens and reads file (as a stream?)
with open('my_file.json', 'r') as source:
    file_contents = source.read()

print(file_contents)

# parses the JSON string back to a python object (e.g dict)
my_group_back_as_dict = json.loads(file_contents)

# e.g. getting output from file
print(my_group_back_as_dict['Nash']['job'])  # nash's job
print(my_group_back_as_dict['Jill']['relationships'])   # jill's relationships


# ###############################

# opening & reading computer files in python
# opening
new_file = open('mydata.txt')
print(type(new_file))

# reading the text (as a string) by treating file as iterable
# [x for x in new_file]
# print("1st try: " + str([x for x in new_file]))  # to show in debug console
# ## if the code(line 66) is run again, it gives an empty list (-> []) because the file has finishied being read, so, to "rewind the tape":
# new_file.seek(0)
# [y for y in new_file]
# print("2nd try: " + str([y for y in new_file]))
# new_file.close()

    # ## ABOVE CODE IS NOT WORKING (YET)...Try the lines below when reading files

new_file.seek(0)  # sets the position of the read/write pointer in the file
first_line = new_file.readline() # consecutive function starting at 1st line
print(first_line)
second_line = new_file.readline() # must follow after 1st .readline() to give the 2nd line(same goes for higher numbers)
print(second_line)

# this block is what was being tested in line 114-117 (BUT IT DID NOT WORK THERE & works here...due to different forms of file opening??)
print('seek & read\n')
new_file.seek(11)
print(new_file.read(4))

# ## this block tests higher numbers & blank space & output when reading beyond text line_number (Which is currently 8 including space)
# ln3 = new_file.readline()
# print("line 3: " + ln3)
# ln4 = new_file.readline()
# print("line 4: " + ln4)
# ln5 = new_file.readline()
# print("line 5: " + ln5)
# ln6 = new_file.readline()
# print("line 6: " + ln6)
# ln7 = new_file.readline()
# print("line 7: " + ln7)
# ln8 = new_file.readline()
# print("line 8: " + ln8)
# ln9 = new_file.readline()
# print("line 9: " + ln9)
# new_file.close()

# to read whole remaing file (even if that is everything i.e. if the file hasn't been read)
# new_file.seek(0)  # commented out because line 76-80 ((1) it's already been written & (2) this is not the beginning of the text)
rest_of_newfile = new_file.read() # due to lines 82-85, this has more bits of code missing
print(rest_of_newfile)
# testing code from line 114-117 (that only worked in line 82-85)...to see effect of differeent forms of opening
# rest_of_newfile.seek(0) # add after running code to check if it will fix anything
# rest_of_newfile.seek(11)
# print(rest_of_newfile.read(4))
new_file.close()  # so that next line of code will work

# opening & reading entire file in one line of code
easy_openread = open('mydata.txt').read()
print("\n easy_or: \n" + easy_openread)

# reading certain characters
#new_file.seek(5)  # will not work as file has been closed
#easy_openread.seek(11)
#easy_openread.read(4)
# NB: file exists here as string, so, read & seek cannot be used until filestring is converted back to orig (file) format:
from io import StringIO
string_as_file = StringIO(easy_openread)
string_as_file.seek(11)
print(string_as_file.read(4))


# creating a new file from a string in memory
# writing the file text
with open('mywrittenfile', 'w') as target:
    target.write('This')
    target.write(' is a')
    target.write(' sentence.')

# reading the written file
with open('mywrittenfile', 'r') as source:
    print("This is the file I have written: \n" + source.read())

# adding more text to the file
with open('mywrittenfile', 'a') as target:  # using 'w' instead of 'a' will overwrite existing file (instead of adding to it)
    target.write(' I added')
    target.write(' this new sentence')
    target.write(' using "append".')
# REreading the appended file
with open('mywrittenfile', 'r') as source:
    print(source.read())