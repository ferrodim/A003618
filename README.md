###### Description
It calculates first X numbers from "Largest n-digit prime" sequence.

See http://oeis.org/A003618/list for details

###### Installation
* apt install python3
* pip3 install bitarray

###### How to run
* `./run.8.sh > result.8.log` // 12MB RAM, 16 digits or less, <1 minute
* `./run.9.sh > result.9.log` // 120MB RAM, 18 digits or less, ~5 minutes
* `./run.10.sh > result.10.log` // 1.2GB RAM, 20 digits or less, ~2 hour
* `./run.11.sh > result.11.log` // 12GB RAM, 22 digits or less, ~18 hours
* `./run.12.sh > result.12.log` // 120GB RAM, 24 digits or less, duration unknown

###### How to read
```
$ grep prime result.11.log 
9999999999999999999973 is a biggest 22 digit prime
999999999999999999899 is a biggest 21 digit prime
99999999999999999989 is a biggest 20 digit prime
9999999999999999961 is a biggest 19 digit prime
999999999999999989 is a biggest 18 digit prime
99999999999999997 is a biggest 17 digit prime
9999999999999937 is a biggest 16 digit prime
999999999999989 is a biggest 15 digit prime
99999999999973 is a biggest 14 digit prime
9999999999971 is a biggest 13 digit prime
999999999989 is a biggest 12 digit prime
99999999977 is a biggest 11 digit prime
9999999967 is a biggest 10 digit prime
999999937 is a biggest 9 digit prime
99999989 is a biggest 8 digit prime
9999991 is a biggest 7 digit prime
999983 is a biggest 6 digit prime
99991 is a biggest 5 digit prime
9973 is a biggest 4 digit prime
997 is a biggest 3 digit prime
97 is a biggest 2 digit prime
```

```
$ grep prime result.11.log | tac | tr -d 'a-z'
97    2  
997    3  
9973    4  
99991    5  
999983    6  
9999991    7  
99999989    8  
999999937    9  
9999999967    10  
99999999977    11  
999999999989    12  
9999999999971    13  
99999999999973    14  
999999999999989    15  
9999999999999937    16  
99999999999999997    17  
999999999999999989    18  
9999999999999999961    19  
99999999999999999989    20  
999999999999999999899    21  
9999999999999999999973    22
```

