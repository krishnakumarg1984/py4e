import re

fname = input("Enter the name of the file: ")

if len(fname) < 1:
    fname = "regex_sum_838484.txt"

try:
    fhandle = open(fname)
except:
    print("Unable to open this file. Quitting!")
    quit()

print(sum([int(num_list) for num_list in re.findall("[0-9]+", fhandle.read())]))
# print(len(num_list))
