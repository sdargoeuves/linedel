# LINEDEL
This python function allows you to delete a specified line from a file. The idea is to quickly remove an SSH key from your known host once a device has been replaced.
To do so, here is how you can use this function:

## Default file - SSH known hosts
```
python3 linedel.py 4
```
By using this function with a integer after the name of the function means the line 4 of the file "~/.ssh/known_hosts" will be deleted.


## Specify a file
```
python3 linedel.py ~/linedel/1to100.txt 4
```
You can also specified the file you want to remove the line from.
