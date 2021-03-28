# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail
# address to a count_dict of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("Unable to open the file. Quitting!")
    quit()

count_dict = dict()
for line in handle:
    if line.startswith("From "):
        words_in_line = line.split()
        if len(words_in_line) < 2:
            continue
        email_sender = words_in_line[1]
        count_dict[email_sender] = count_dict.get(email_sender, 0) + 1

# print(count_dict)
big_count = None

for name, count in count_dict.items():
    if big_count is None or count > big_count:
        big_count = count
        most_freq_sender = name

print(most_freq_sender, big_count)
