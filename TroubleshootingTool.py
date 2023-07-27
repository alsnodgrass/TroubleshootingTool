"""
Author:     Austin Snodgrass
Name:       Troubleshooting Tool
Date:       07/27/2023
Purpose:    Creating a user interface to allow users to input a host name and select a troubleshooting
    tool (ping, pathping, tracert, systeminfo) and receive the CLI output in the same window to assist
    with troubleshooting efforts
Issues:     1) Still need to figure out how to read command line output to GUI. May need to write output
    to file and read file data back to UI
            2) Still need to setup output window in UI
            3) Program should run as .exe that can be placed on desktop
"""

import subprocess
import PySimpleGUI as psg

def ping():
    commands = 0

def pathping():
    commands = 0

def traceroute():
    commands = 0

def systeminfo():
    commands = 0

host_input = [
    [
        psg.Text('Host Name: '),
        psg.In(size = (20, 1), enable_events = True, key = 'HOST', justification = 'right')
    ]
]

tool_select = [
    [
        psg.Checkbox('Ping', key = 'PING'),
        psg.Push(),
        psg.Checkbox('Path Ping', key = 'PATHPING')
    ],
    [
        psg.Checkbox('Trace Route', key = 'TRACEROUTE'),
        psg.Push(),
        psg.Checkbox('System Info', key = 'SYSTEMINFO')
    ],
    [
        psg.Button('Run Commands', size = (20, 1), key = 'RUNCOMMANDS')
    ]
]

layout = [
    [
        psg.Column(host_input)
    ],
    [
        psg.Column(tool_select)
    ]
]

gui = psg.Window('Troubleshooting Tool', layout)

while True:
    event, values = gui.read()

    if event == 'RUNCOMMANDS':
        if 'PING' == True:
            ping()
        if 'PATHPING' == True:
            pathping()
        if 'TRACEROUTE' == True:
            traceroute()
        if 'SYSTEMINFO' == True:
            systeminfo()
    if event == psg.WIN_CLOSED:
        break

gui.close()




"""
host = str(input("Host name: "))

command = [str(input('Command: ')), host]

print(subprocess.call(command))
"""