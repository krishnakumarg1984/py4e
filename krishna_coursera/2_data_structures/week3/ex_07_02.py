#  7.2 Write a program that prompts for a file name, then opens that file and
#  reads through the file, looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as shown
# below. Do not use the sum() function or a variable named sum in your solution.
#
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Error: Unable to open file", fname)
    quit()

count_spam_confidence_lines = 0
# spam_confidence_avg = None
spam_confidence_total = 0
for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count_spam_confidence_lines += 1
    colon_loc = line.find(":")
    try:
        # if spam_confidence_avg is None:
        #     spam_confidence_avg = float(line[colon_loc + 1 :])
        # else:
        #     spam_confidence_avg = (
        #         spam_confidence_avg * (count_spam_confidence_lines - 1)
        #         + float(line[colon_loc + 1 :])
        #     ) / count_spam_confidence_lines
        spam_confidence_total += float(line[colon_loc + 1 :])
    except:
        print("The parsed value in this line is not a number")
        quit()

# print("Done")
print("Average spam confidence:", spam_confidence_total / count_spam_confidence_lines)
