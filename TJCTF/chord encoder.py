f = open('notes.txt').read().split()
chords={}
l = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7'}
for i in open('chords.txt').readlines():
	c, n = i.strip().split()
	chords[n]=c
flag=""
ch=""
for i in f:
    flag+=chords[i]+" "
for i in flag.split():
    if(i in l):
        ch+=l[i]
    else:
        ch+=i
print(ch.decode('hex'))
