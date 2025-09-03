@echo off
echo Installing Sansam requirements...
pip install pyinstaller

echo Building Sansam executable...
pyinstaller --clean sansam.spec

echo Creating distribution package...
mkdir dist\sansam-package
copy dist\sansam\sansam.exe dist\sansam-package\
copy examples\*.sans dist\sansam-package\examples\
copy README.md dist\sansam-package\

echo Creating environment setup...
echo @echo off > dist\sansam-package\install.bat
echo setx PATH "%%PATH%%;%%~dp0" >> dist\sansam-package\install.bat
echo echo Sansam has been installed! You can now run .sans files using: sansam yourfile.sans >> dist\sansam-package\install.bat

echo Package created successfully in dist\sansam-package
echo To distribute, zip the contents of dist\sansam-package
