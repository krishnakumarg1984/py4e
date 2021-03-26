# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

num_start_idx = text.find("0")
num = text[num_start_idx:]
try:
    float_num = float(num)
    print(float_num)
except:
    print("Cannot convert the found substring to float")
