@echo off
echo Setting up Sansam Demo Environment...

:: Create demo directory
mkdir C:\SansamDemo 2>nul

:: Copy required files
echo Copying Sansam executable and example program...
copy "%~dp0dist\sansam.exe" "C:\SansamDemo" /Y
copy "%~dp0demo\hello.sans" "C:\SansamDemo" /Y

:: Add to PATH temporarily
set "PATH=%PATH%;C:\SansamDemo"

echo.
echo Demo environment is ready!
echo.
echo Running hello.sans program...
echo =============================
cd C:\SansamDemo
sansam.exe hello.sans

echo.
echo =============================
echo Demo completed! Press any key to exit...
pause
