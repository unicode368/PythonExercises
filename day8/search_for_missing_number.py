a = [1,2,5,8,9,11]
min_dif = float('inf')


for i in range(0, len(a) - 1):
    if min_dif > a[i + 1] - a[i]:
        min_dif = a[i + 1] - a[i]

for i in range(0, len(a) - 1):
   if min_dif < a[i + 1] - a[i]:
       coef = (a[i + 1] - a[i]) // min_dif - 1
       dif = min_dif
       while coef > 0:
           print(a[i] + min_dif)
           min_dif += dif
           coef -= 1
       min_dif = dif