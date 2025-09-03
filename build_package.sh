#!/bin/bash

echo "Installing Sansam requirements..."
pip install pyinstaller

echo "Building Sansam executable..."
pyinstaller --clean sansam.spec

echo "Creating distribution package..."
mkdir -p dist/sansam-package/examples
cp dist/sansam/sansam dist/sansam-package/
cp examples/*.sans dist/sansam-package/examples/
cp README.md dist/sansam-package/

echo "Creating environment setup..."
cat > dist/sansam-package/install.sh << 'EOL'
#!/bin/bash
INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"
cp sansam "$INSTALL_DIR/"
echo "export PATH=\$PATH:\$HOME/.local/bin" >> ~/.bashrc
source ~/.bashrc
echo "Sansam has been installed! You can now run .sans files using: sansam yourfile.sans"
EOL

chmod +x dist/sansam-package/install.sh

echo "Package created successfully in dist/sansam-package"
echo "To distribute, create a tarball of dist/sansam-package"
