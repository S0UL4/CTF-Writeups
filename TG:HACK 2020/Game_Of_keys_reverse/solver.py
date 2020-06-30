import base64
from itertools import cycle

class myGame:

    def __init__(self, xdim=4, ydim=4):
        self.x = xdim
        self.y = ydim
        self.matrix = []
        for i in range(self.x):
            row = []
            for j in range(self.y):
                row.append(0)

            self.matrix.append(row)

    def make_keys(self, *args, **kwargs):
        words = []
        with open('wordlist.txt') as (f):
            for line in f:
                words.append(line.strip())

            for i in range(self.x):
                for j in range(self.y):
                    self.matrix[j][i] = words[(i + j)]
        keyArray = []
        
        keyArray.append(self.matrix[args[0]][args[1]])
        keyArray.append(self.matrix[args[2]][args[3]])
        key = ''
        for k in keyArray:
            key = key.strip() + str(k).strip()
        key="aa1baa1faa1baa1faa1baa1faa1baa1faa1b"
        return key

    def checkdata(self, key):
        f = base64.b64decode('NSYDUhoVWQ8SQVcOAAYRFQkORA4FQVMDQQ5fQhUEWUYMDl4MHA==')
        data = f.decode('ascii')
        #TG20{this flag should be onthe#moon}
        p=""
        for c,k in zip(data,cycle(key)):
            p+=chr(ord(c)^ord(k))
        print(p)   
        #print(chr(3^49))
        #print(chr(49))   
       # c = ''.join(print((chr(ord(c) ^ ord(k))) for c, k in zip(data, cycle(key))))
        #print(c)
        #print('%s ^ %s = %s' % (data, key, c))


if __name__ == '__main__':
    mgame = myGame(25, 25)
    data = mgame.make_keys(1,1,1,1)
    mgame.checkdata(data)

f = base64.b64decode('NSYDUhoVWQ8SQVcOAAYRFQkORA4FQVMDQQ5fQhUEWUYMDl4MHA==')
data = f.decode('ascii')
ch="TG20{this flag should be on xxx moon}"
key="aa1baa1faa1baa1faa1baa1faa1baa1faa1b"
p=""
for c in range(len(data)):
    for i in range(0,255):
        if(chr(ord(data[c])^i)==ch[c]):
            p+=chr(i)
print(p)
