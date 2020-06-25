import math
import random
from datetime import datetime
import time
timestamp = time.mktime(time.strptime('2020-05-29 22:00:00', '%Y-%m-%d %H:%M:%S'))
f='150 2 103 102 192 216 52 128 9 144 10 201 209 226 22 10 80 5 102 195 23 71 77 63 111 116 219 22 113 89 187 232 198 53 146 112 119 209 64 79 236 179'.split()
random.seed(int(timestamp))
flag=''
for i in range(42):
    x=random.randint(0, 255)
    flag+=str(x^int(f[i]))+' '
print(''.join([chr(int(x)) for x in flag.split()]))
