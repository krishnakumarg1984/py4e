import re

fname = input("Enter the name of the file: ")

if len(fname) < 1:
    fname = "regex_sum_838484.txt"

try:
    fhandle = open(fname)
except:
    print("Unable to open this file. Quitting!")
    quit()

total = 0
for line in fhandle:
    line = line.rstrip()
    str_num_list = re.findall("[0-9]+", line)
    if len(str_num_list) == 0:
        continue
    for num in str_num_list:
        total += int(num)

print(total)
