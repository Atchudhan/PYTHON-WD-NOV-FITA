a=int(input("Enter the year:"))
if(a%4==0 and a%100!=0 or a%400==0):
    b=29
else:
    b=28
print("jan:31")
print("feb:",b)
print("mar:31")
print("arp:30")
print("may:31")
print("jun:30")
print("july:31")
print("aug:31")
print("sep:30")
print("oct:31")
print("nov:30")
print("dec:31")
