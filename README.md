# Introduction to Github


## Table of contents
* [General info](#general-info)
* [C](#c)
* [Python](#python)
* [Sources](#sources)


## General info
This project was created by myself to get used to the GitHub environment, and for learning the proper way to document work, make commits, and push from my local machine onto the GitHub website. This is also the place I'll place files for code snippets that are meant to test how certain features work, or just for general testing purposes.


## C
### hello_world.c
A small C program meant to print out hello world when run from the terminal
```
$ gcc -o hello_world hello_world.c
$ ./hello_world
```
### roll_dice.c
A C program that will roll dice values for you, default is one six sided dice
```
$ gcc -o roll_dice roll_dice.c
$ ./roll_dice
$ ./roll_dice --d=12 --n=3
```
Optional Arguements
* d option specifies the type of dice (4, 6, 8, 10, 12, or 20 sided)
* n option specifies the number of dice to roll


## Python
### venv setup
How to set up the virtual environment for any of these programs
All programs here are set up in their own virtual environments which have been omitted from the github
```
$ python3 -m venv /Python/hello_world
$ source Python/hello_world/bin/activate
```
And then to deactivate the virtual environment
```
$ deactivate
```
### hello_world.py
A small Python program which will print out a greeting along with a random number and the current date
```
$ source /bin/activate
$ python hello_world.py
```


## Sources
* http://akira.ruc.dk/~keld/teaching/CAN_e14/Readings/How%20to%20Compile%20and%20Run%20a%20C%20Program%20on%20Ubuntu%20Linux.pdf
* https://linuxprograms.wordpress.com/2012/06/22/c-getopt_long-example-accessing-command-line-arguments/
