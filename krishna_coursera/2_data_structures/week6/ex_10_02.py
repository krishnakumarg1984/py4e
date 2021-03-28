# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("Unable to open the file. Quitting")
    quit()

hour_counts_dict = dict()
for line in handle:
    if line.startswith("From "):
        words_in_line = line.split()
        if len(words_in_line) < 6:
            continue
        sent_time_full = words_in_line[5]
        sent_time_hh_mm_ss_list = sent_time_full.split(":")
        sent_time_hours = sent_time_hh_mm_ss_list[0]
        hour_counts_dict[sent_time_hours] = hour_counts_dict.get(sent_time_hours, 0) + 1

sorted_hist_hour_counts = sorted([(k, v) for k, v in hour_counts_dict.items()])

for (hour, counts) in sorted_hist_hour_counts:
    print(hour, counts)
