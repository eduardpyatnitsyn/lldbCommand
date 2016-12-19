#!/usr/bin/python

import lldb
import shlex


def pp(debugger, command, result, internal_dict):
    target = debugger.GetSelectedTarget()
    process = target.GetProcess()
    command_args = shlex.split(command)

    for thread in process:
        for frame in thread:
            if ''.join(command_args) in str(frame): 
                print >>result, str(frame)


def pf(debugger, command, result, internal_dict):
    target = debugger.GetSelectedTarget()
    process = target.GetProcess()
    thread = process.GetSelectedThread()
    command_args = shlex.split(command)

    for frame in thread:
        if ''.join(command_args) in str(frame): 
            print >>result, str(frame)


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f print_command.pp pp')
    debugger.HandleCommand('command script add -f print_command.pf pf')
    print 'The "pf" python command has been installed and is ready for use.'
    print 'The "pp" python command has been installed and is ready for use.'
