names = ['evan', 'colin', 'brian']

for name in names:
    print(name)

sum = 0
for x in range(101):
    sum = sum+x
print(sum)

n = 0
while n < 10:
    n = n+1
    if n % 2 == 0:
        continue
    print(n)

s = 0
while s < 3:
    print('hello', name[s])
    s = s+1
