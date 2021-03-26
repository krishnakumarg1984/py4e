hrs = input("Enter Hours:")
h = float(hrs)

rph = input("Enter Hourly Rate:")
r = float(rph)

if h < 40.0:
    pay = h*r
else:
    pay = (40.0 + (h-40)*1.5)*r

print(pay)
