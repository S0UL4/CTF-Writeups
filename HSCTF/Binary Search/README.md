``` 
My little brother who is in kindergarten was given this to him by his teacher. He wasn't able to solve it, but can you?
Note: 0 is black, 1 is white. The entire flag is hidden inside the word search, including flag{}. The flag may also be backwards or diagonally hidden.
```



So instead of  playing a word search with letters, we're now playing with a 1000x1000 grid of bits ( 0 and 1 ).
The strategy is to recursively test each bit for a match to flag{, and if a match is found, iterate over all 8 possible directions (north, north-east, east, etc..) and test for the next bit.

