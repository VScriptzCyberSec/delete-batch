@echo off
REM This batch file deletes all files in a specified directory

REM Specify the target directory
SET targetDir=C:\path\to\your\directory

REM Ensure the directory exists
IF NOT EXIST "%targetDir%" (
    ECHO The directory "%targetDir%" does not exist.
    EXIT /B 1
)

REM Delete all files in the specified directory
DEL /Q "%targetDir%\*.*"

REM Inform the user
ECHO All files in "%targetDir%" have been deleted.

REM End of script
