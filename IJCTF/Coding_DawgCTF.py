from pwn import *
p=remote('arthurashe.ctf.umbccd.io',8411)
msg=p.recv()
p.sendline('y')
flag=""
while(True):
    try:
        msg=p.recv()
    
        if('You' in msg):
            print(msg)
            break

        msg=msg.split()
        dictc={msg[-1].split('-')[0]:"0",msg[-1].split('-')[1][:len(msg[-1].split('-')[1])-1]:"1"}
        search=msg[4]
        if(search in dictc.keys()):
            p.sendline(dictc[search])
            flag+=dictc[search]
        elif not(search in dictc.keys()):
            l=[]
            for i in dictc.keys():
                try:
                    l.append(eval(i))
                except:
                    print('...')
            if(len(l)==2):
                p.sendline(dictc[str(max(l))])
                flag+=dictc[str(max(l))]
            else:
                p.sendline(dictc[str(l[0])])
                flag+=dictc[str(l[0])]
        else:
            p.sendline(dictc.keys()[max(dictc.keys())])
            flag+=dictc.keys()[max(dictc.keys())]
    except:
        print(msg)
        break
print(flag)
p.close()

