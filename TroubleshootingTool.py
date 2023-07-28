"""
Author:     Austin Snodgrass
Name:       Troubleshooting Tool
Date:       07/28/2023
Purpose:    Creating a user interface to allow users to input a host name and select a troubleshooting
    tool (ping, pathping, tracert, systeminfo) and receive the CMD output in the same window to assist
    with troubleshooting efforts
"""

# Importing packages for console access and UI and setting UI theme
import subprocess
import PySimpleGUI as psg
psg.theme('DarkBlack')

# Defining Ping, Pathping, Trace Route and System Info functions to run the specified command for each
# button with the host name given by the user. 'command' variable creates a string holding the command
# to be passsed to the console. 'pipe' variable initiates the subprocess library class Popen to
# interact with the console and read output with stdout. 'line' variable reads each line of output and
# is converted to a string as the 'lineString' variable to be printed to the UI. Console read is in a
# while loop that breaks and ends the function once there is no more data to be read
def ping():
    command = 'ping ' + str(values['HOST'])
    pipe = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    while True:
        line = pipe.stdout.readline()
        if line:
            lineString = str(line)
            gui['OUTPUT'].print(lineString[2:-5])
            gui.refresh()
        if not line:
            break
def pathping():
    command = 'pathping -q 10 ' + str(values['HOST'])
    pipe = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    while True:
        line = pipe.stdout.readline()
        if line:
            lineString = str(line)
            gui['OUTPUT'].print(lineString[2:-5])
            gui.refresh()
        if not line:
            break
def traceroute():
    command = 'tracert ' + str(values['HOST'])
    pipe = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    while True:         
        line = pipe.stdout.readline()
        if line:
            lineString = str(line)
            gui['OUTPUT'].print(lineString[2:-5])
            gui.refresh()
        if not line:
            break
def systeminfo():
    command = 'systeminfo /s ' + str(values['HOST'])
    pipe = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    while True:         
        line = pipe.stdout.readline()
        if line:
            lineString = str(line)
            gui['OUTPUT'].print(lineString[2:-5])
            gui.refresh()
        if not line:
            break

# Setting up the text box and buttons to allow for user input and interaction
host_input = [
    [
        psg.Text('Host Name: '),
        psg.In(size = (11, 1), enable_events = True, key = 'HOST', justification = 'right')
    ],
    [
        psg.Push()
    ],
    [
        psg.Button('Ping', size = (20, 1), key = 'PING')
    ],
    [
        psg.Push()
    ],
    [
        psg.Button('Path Ping', size = (20, 1), key = 'PATHPING')
    ],
    [
        psg.Push()
    ],
    [
        psg.Button('Trace Route', size = (20, 1), key = 'TRACEROUTE')
    ],
    [
        psg.Push()
    ],
    [
        psg.Button('System Info', size = (20, 1), key = 'SYSTEMINFO')
    ]
]

# Setting up the output window to display console information
output_window = [
    [
        psg.Multiline(key = 'OUTPUT', size = (500, 300))
    ]
]

# Setting up the layout to include user interaction and display areas
layout = [
    [
        psg.Column(host_input),
        psg.VSeperator(),
        psg.Column(output_window)
    ]
]

# Setting up GUI instance and initializing the layout we created
gui = psg.Window('Troubleshooting Tool', layout, size = (800, 300))

# While loop created to allow user to reuse program until they manually exit. If statements initialize
# the correct function based on which button the user clicks
while True:
    event, values = gui.read()

    if event == 'PING':
        ping()
    if event == 'PATHPING':
        pathping()
    if event == 'TRACEROUTE':
        traceroute()
    if event == 'SYSTEMINFO':
        systeminfo()
    if event == psg.WIN_CLOSED:
        break

gui.close()