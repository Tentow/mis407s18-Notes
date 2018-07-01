# ICA01 Recap

See what Windows drives are "mounted" and their locations:
`mount`

Change to your user share drive:
`cd /u`

Make a directory named MIS407:
`mkdir MIS407`

Change the current directory to the new MIS407 directory:
`cd MIS407`

List files in the current directory:
`ls`

List files in a specific directory (e.g., "C:\ProgramData"): 
`ls /c/ProgramData`

Show the current directory:
`pwd`

Echo a string:
`echo 'Hello There'`

Write the string into a file using output redirection:
`echo 'Hello There' >> hello.txt`

See the contents of a file:
`cat hello.txt`

Copy a file, and verify it is in the directory:
`cp hello.txt hello2.txt`
`ls`

Rename a file ("mv" -- move it):
`mv hello2.txt hello3.txt`

Delete a file:
`rm hello3.txt`

Use --help on the command line for more information on usage, e.g.:
`ls --help`
> Usage: ls [OPTION]... [FILE]... List information about the FILEs
> (the current directory by default). Sort entries alphabetically...

Write a simple Python program:
`echo 'print("Hello, World")' >> hello.py`

Run the Python program:
`python hello.py`
