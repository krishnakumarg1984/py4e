def computepay(h, r):
    if h < 40.0:
        p = h * r
    else:
        # p = 40.0*r + (h-40.0)*1.5*r
        p = r * (40.0 + (h - 40.0) * 1.5)
    return p


hrs = input("Enter Hours:")
rph = input("Enter Rate Per Hour:")
hrs = float(hrs)
rph = float(rph)
p = computepay(hrs, rph)
print("Pay", p)
