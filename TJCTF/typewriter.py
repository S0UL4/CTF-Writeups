ch1='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
typ='q w e r t y u i o p a s d f g h j k l z x c v b n m'.split()
flagenc='zpezy{fg_dgkt_atn_pqdl}'
sol={}
flag=''
for i in range(len(typ)):
    sol[typ[i]]=ch1[i]
for i in flagenc:
    try:
        flag+=sol[i]
    except:
        flag+=i
print(flag)
