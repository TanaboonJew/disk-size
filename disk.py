import os

def get_storage_info():
    print("Storage Devices Info:")
    print("---------------------------------")
    
    with os.popen("df -h") as df_output:
        lines = df_output.readlines()
    
    for line in lines[1:]:  # Skip header
        columns = line.split()
        if columns[0].startswith("/dev/"):
            device, size, avail = columns[0], columns[1], columns[3]
            print(f"Device Path: {device}")
            print(f"Total Capacity: {size}")
            print(f"Unused Capacity: {avail}")
            print("---------------------------------")

if __name__ == "__main__":
    get_storage_info()
