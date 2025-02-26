import psutil

def get_storage_info():
    partitions = psutil.disk_partitions()
    
    print("Storage Devices Info:")
    print("---------------------------------")
    for partition in partitions:
        try:
            size = psutil.disk_usage(partition.mountpoint)
            print(f"Device Path: {partition.device}")
            print(f"Total Capacity: {size.total / (1024**3):.2f} GB")
            print(f"Unused Capacity: {size.free / (1024**3):.2f} GB")
            print("---------------------------------")
        except PermissionError:
            print(f"Device Path: {partition.device}")
            print("Permission denied - Unable to access details")
            print("---------------------------------")
            continue

if __name__ == "__main__":
    get_storage_info()
