from __future__ import print_function

class Colors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

print("")
print("""This script is going to recreate an apikey.py file 
please press 'Ctrl+C' if you don't want to do it 
and a 'Enter' if you do want it""")
print("")
raw_input("?")
print("")
print (Colors.BLUE + "Please, paste your api key:" + Colors.END)

user_input = raw_input("> ")

keyfile = open("apikey.py", 'w')
keyfile.write("key = '" + user_input + "'" + "\n")
keyfile.close()
