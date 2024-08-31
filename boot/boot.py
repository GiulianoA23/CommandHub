# boot.py: This file initializes the system and starts the kernel.

def boot_system():
    print("Bootloader: Initializing system...")
    from kernel import kernel
    kernel.start()

if __name__ == "__main__":
    boot_system()
