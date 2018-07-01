""" Connect to the specified sqlite3 database and
    execute commands entered by the user """

import sqlite3
import sys

if len(sys.argv) == 1:
    print('Usage: {} sqlite-filename'.format(sys.argv[0]))
    sys.exit(1)

sqlite_file = sys.argv[1]

conn = sqlite3.connect(sqlite_file)

done = False
while not done:
    cmd = input('Enter SQL command or \'quit\': ')
    if cmd == 'quit':
        done = True
    else:
        try:
            cur = conn.cursor()
            cur.execute(cmd)
            # Get the column names
            names = tuple(description[0] for description in cur.description)
            print(names)
            for row in cur.fetchall():
                print(row)
        except Exception as e:
            print(e)  # Show the exception to the user
