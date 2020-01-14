# Version of the EUPL
VERSION = 0.1

# Prompt
PROMPT = 'eupl:~$ '

# ASCII banner to show in the EUPL startup
BANNER = """
 ______     __  __     ______   __        
/\  ___\   /\ \/\ \   /\  == \ /\ \       
\ \  __\   \ \ \_\ \  \ \  _-/ \ \ \____  
 \ \_____\  \ \_____\  \ \_\    \ \_____\ 
  \/_____/   \/_____/   \/_/     \/_____/ 

Welcome to UEPL version {}                                     
""".format(VERSION)

# Command list
COMMANDS = [
    'ver',
    'exit',
    'add',
    'mult',
    'mem',
    'say',
    'info',
    'bin',
    'get',
    'man',
    # Add commands above
    'cmd'
]

MANUAL = {
    'ver': 'Outputs the UEPL version',
    'exit': 'Closes the program',
    'add': 'Sums two numbers (e.g. add 2 1)',
    'mult': 'Multiplies teo numbers (e.g. mult 2 2)',
    'mem': 'Shows the commands memory',
    'say': 'Prints a string',
    'info': 'Gets info from the system',
    'bin': 'Converts a decimal number into binary',
    'get': 'Makes a GET HTTP request and outputs to a file',
    'man': 'Instructions for every EUPL command',
    'cmd': 'Shows the list of commands'
}
