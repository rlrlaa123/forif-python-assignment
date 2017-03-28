#1주차 과제 4

a = "101112131415"
b = list(a)
b = [int(x) for x in b]
#print(sum(b))

a = "101112131415"
#print int(a[0:2])+int(a[2:4])+int(a[4:6])+int(a[6:8])+int(a[8:10])+int(a[10:12])
b=0
for i in range(0,6):
   b += int(a[i*2:i*2+2])
print b
