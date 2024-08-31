# echo.py: Mimics the echo command in Unix systems.

def run(command):
    _, *args = command.split()
    print(" ".join(args))
