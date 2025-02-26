# disk-size
    First, I chose Python as it was easier to work with and is typically pre-installed on most Ubuntu systems. However, the requirements specify that I cannot "rely on or pull in any packages which are not available in the standard Ubuntu package repository." I was unsure whether `psutil`, which I wanted to use, was available by default. This left me with Python's built-in `os` module, but since I was working with system commands anyway, I realized I would be better off using Bash.

    The problem with Bash is that, while I already know how the `df -h` command works, I needed to transform it into a script that outputs only the **Path**, **Total Capacity**, and **Available Capacity**. The solution was to use `grep` to filter the lines containing storage device information and `awk` to extract and print specific columns. With this approach, I was able to get the exact output I needed in a simple and efficient way.
