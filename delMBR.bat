@echo off
:: WARNING: This script will delete the MBR of the specified drive.
:: Ensure you have backups of any important data before proceeding.
:: Use at your own risk.

:: Define the target drive (e.g., \\.\PhysicalDrive0)
set TARGET_DRIVE=\\.\PhysicalDrive0

:: Confirm the action
echo WARNING: This will delete the MBR of %TARGET_DRIVE%.
echo This action is destructive and will render the drive unbootable.
set /p CONFIRM=Are you sure you want to continue? (yes/no): 
if /I "%CONFIRM%" NEQ "yes" (
    echo Operation cancelled.
    exit /B
)

:: Use dd to write zeros to the first 512 bytes of the target drive
:: Ensure dd.exe is in the same directory as this batch file or in the system PATH.
echo Deleting the MBR of %TARGET_DRIVE%...
dd if=\\.\nul of=%TARGET_DRIVE% bs=512 count=1

echo MBR deletion complete.
