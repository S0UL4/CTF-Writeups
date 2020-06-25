flagg=""
f=open('flag','r').read()
f=f.split()
for i in range(len(f)):
    f[i]=f[i][::-1]
for i in range(len(f)):
    flagg+=f[len(f)-i-1]+" "
gotcha="89 50 4e 47 "+flagg
data = bytes.fromhex(gotcha)
with open('mar7ba.png', 'wb') as file:
    file.write(data)
#bingoo___the_flag_is_ijctf{17$_$1mp7e}
