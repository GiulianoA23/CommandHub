# PyNix OS

**PyNix OS** is a lightweight, Python-powered operating system designed with a Unix-like structure. It offers a simple yet powerful environment for learning operating system fundamentals, Python scripting, and command-line interfaces.

## Features

- **Unix-Like Structure**: Adheres to traditional Unix conventions with directories like `/boot`, `/kernel`, `/bin`, `/lib`, `/etc`, and `/home`.
- **Python-Based**: Entirely written in Python, making it accessible and easy to modify or extend.
- **Lightweight**: Optimized for minimal resource consumption, suitable for older hardware or virtual machines.
- **Educational**: Ideal for learning OS design, command processing, and file system management.
- **Customizable**: Easily extend the OS with new commands, utilities, or configurations using Python.

## Project Structure

```
/boot       - Contains bootloader files.
/kernel     - Core OS functionalities.
/bin        - Essential user commands.
/lib        - Essential libraries.
/etc        - Configuration files.
/home       - User home directories.
/Docs       - Documentation for the OS.
```

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pynix-os.git
   cd pynix-os
   ```

2. **Run PyNix OS**:
   Start the OS by running the `main.py` script:
   ```bash
   python3 main.py
   ```

3. **Use Built-In Commands**:
   - `echo`: Print text to the terminal.
   - `ls`: List contents of the current directory.
   - `exit`: Shut down the OS.

## Building the ISO

To compile PyNix OS into a bootable ISO, follow these steps:

1. Ensure you have `xorriso` and `grub-pc-bin` installed:
   ```bash
   sudo apt-get install xorriso grub-pc-bin
   ```

2. Run the provided GitHub Action or use the following command:
   ```bash
   xorriso -as mkisofs \
   -R -J -c boot/grub/stage2_eltorito \
   -b boot/grub/i386-pc/eltorito.img \
   -no-emul-boot -boot-load-size 4 -boot-info-table \
   -o pynix_os.iso iso/
   ```

3. The ISO file will be created as `pynix_os.iso`.

## Contributing

Contributions are welcome! Feel free to submit issues, pull requests, or suggestions to improve PyNix OS.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**PyNix OS**: Learn, explore, and experiment with the fundamentals of operating systems using the power and simplicity of Python.
