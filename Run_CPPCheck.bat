REM Check if enough arguments are provided

set SOURCE_PATH=%~1
set DESTINATION_PATH=%~2
echo %DESTINATION_PATH%
REM Path to the Cppcheck executable
set CPPCHECK_PATH="C:\Program Files\Cppcheck\Cppcheck.exe"

REM Run Cppcheck and output to an XML file
%CPPCHECK_PATH% --enable=all --xml --xml-version=2 %SOURCE_PATH% 2> %DESTINATION_PATH%\cppcheck.xml

REM Check if the XML file was created
if not exist "%DESTINATION_PATH%\cppcheck.xml" (
    echo Error: cppcheck.xml was not created.
    exit /b 1
)

REM Run the Python script to convert the XML report to a spreadsheet
python CPP_Check_Report.py %DESTINATION_PATH%

REM Check if the spreadsheet was created
if exist %DESTINATION_PATH%\cppcheck_reports.xlsx (
    echo Spreadsheet generated successfully: %DESTINATION_PATH%\cppcheck_reports.xlsx
    start "" %DESTINATION_PATH%
) else (
    echo Error: Spreadsheet was not created.
    exit /b 1
)

exit /b 0