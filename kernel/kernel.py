# kernel.py: Contains the core functionalities of the OS, managing processes and commands.

import os
import sys
from bin import echo, ls

def start():
    print("Kernel: System started.")
    while True:
        command = input("shell> ")
        execute_command(command)

def execute_command(command):
    # Basic command execution logic
    if command.startswith("echo"):
        echo.run(command)
    elif command.startswith("ls"):
        ls.run(command)
    elif command == "exit":
        print("Kernel: Shutting down...")
        sys.exit(0)
    else:
        print(f"Kernel: Command not found: {command}")
