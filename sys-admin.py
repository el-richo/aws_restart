"""
Ricardo Cereceres
"""
#Exercise 1: Using os.system
import os
import subprocess

os.system("ls")

#Exercise 2: Using subprocess.run
"""
Though os.system() is simple to use because it takes a string argument, it is recommended that you use the more powerful subprocess.run() function. You can use the subprocess module to spawn new processes, connect to input/output/error pipes, and obtain error codes. The subprocess.run() function can take many new arguments, but those additional arguments are optional.

The full list of arguments for subprocess.run() looks like the following list:

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
"""
subprocess.run(["ls","-l","README.md"])

#Exercise 5: Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Exercise 6: Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
