# disk-size

## Overview
First, I chose Python as it was easier to work with and is typically pre-installed on most Ubuntu systems.  
However, the requirements specify that I cannot  
> rely on or pull in any packages which are not available in the standard Ubuntu package repository.

I was unsure whether `psutil`, which I wanted to use, was available by default.  
This left me with Python's built-in `os` module, but since I was working with system commands anyway,  
I realized I would be better off using Bash.

The problem with Bash is that, while I already know how the `df -h` command works, I needed to transform it into a script that outputs only the **Path**, **Total Capacity**, and **Available Capacity**. The solution was to use `grep` to filter the lines containing storage device information and `awk` to extract and print specific columns. With this approach, I was able to get the exact output I needed in a simple and efficient way.

## Build and Run Instructions
### Dependencies
This script requires only standard Linux utilities that are pre-installed on Ubuntu:
- `bash`
- `df`
- `grep`
- `awk`

### How to Run
1. Clone or download the script to your machine.
2. Give execution permission to the script:
   ```bash
   chmod +x storage_info.sh
   ```
3. Run the script:
   ```bash
   ./storage_info.sh
   ```
The output will display the Path, Total Capacity, and Available Capacity of storage devices.