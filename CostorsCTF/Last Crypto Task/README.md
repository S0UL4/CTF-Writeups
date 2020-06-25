``` Author: hasu

Response to Amazon: Nah, I only need to be able to watch 101 Dalmatians.

c6 22 3d 29 c1 c5 9c f5 85 e7 d7 0e 46 e6 21 e7 dd 8d db 43 a0 34 77 04 7f 32 13 8c c9 01 65 78 5f c0 14 8e 33 bf bc 02 21 79 e1 5d d3 46 e0 ca ee 72 c2 26 38 
````
That was My solution for this Task :

``` from Crypto.Util.number import isPrime
def nextPrime(n):
    if isPrime(n):
        return n
    else:
        return nextPrime(n+1)
ch='c6 22 3d 29 c1 c5 9c f5 85 e7 d7 0e 46 e6 21 e7 dd 8d db 43 a0 34 77 04 7f 32 13 8c c9 01 65 78 5f c0 14 8e 33 bf bc 02 21 79 e1 5d d3 46 e0 ca ee 72 c2 26 38'.split()
k=''
for i in ch:
    k+=str(int(i,16))+' '
k=k.split()
m=[]
a=2
j = 2
i=0
while i<len(k):
    if(a%257==int(k[i]) and a%j==0):
        j = nextPrime(j+1)
        m.append(a)
        i=i+1
        a=2
    a=a+1
flag = ""
j = 2
for i in range(0,len(m)):
    flag +=chr(m[i]//j)
    j = nextPrime(j+1)
print(flag)
``` 
```
The Output of our program is : castorsCTF{1f_y0u_g07_th1s_w1th0u7_4ny_h1n7s_r3sp3c7}
```


