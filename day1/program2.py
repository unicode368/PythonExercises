name = input("Enter name:")
subject = input("Enter subject:")
m1 = int(input("Enter m1:"))
while m1 < 0 or m1 > 100:
    m1 = int(input("Enter m1:"))
m2 = int(input("Enter m2:"))
while m2 < 0 or m2 > 100:
    m2 = int(input("Enter m2:"))
m3 = int(input("Enter m3:"))
while m3 < 0 or m3 > 100:
    m3 = int(input("Enter m3:"))
avg = (m1 + m2 + m3) / 3

if 70 <= avg <= 100:
    print("A")
elif 50 <= avg < 70:
    print("B")
elif 35 <= avg < 50:
    print("C")
else:
    print("failed")

