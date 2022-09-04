import math

n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
r = int(input("Enter shift:"))
while r < 0:
    r = int(input("Enter shift:"))

shift = 0
for i in range(1,r + 1):
    shift = 0
    shift += n // 10**int(math.log10(n))
    shift += (n % 10**int(math.log10(n))) * 10
    n = shift
print(n)
