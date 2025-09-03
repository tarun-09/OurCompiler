# Sansam Programming Language

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)

Sansam is a Sanskrit-based programming language that allows you to write programs using Sanskrit terminology. It provides a unique way to write programs while preserving the beauty and richness of the Sanskrit language.

## Features

- Sanskrit-based syntax for natural expression
- Support for modern programming constructs
- Rich standard library of built-in functions
- Cross-platform support (Windows, Linux, macOS)
- Standalone executable distribution

## Installation

### Windows Users
1. Download the latest `sansam-windows.zip` from the releases page
2. Extract the zip file to any location
3. Run `install.bat` as administrator (this will add Sansam to your system PATH)
4. Open a new command prompt and you're ready to use Sansam!

### Linux/Mac Users
1. Download the latest `sansam-unix.tar.gz` from the releases page
2. Extract the archive: `tar -xzf sansam-unix.tar.gz`
3. Navigate to the extracted directory and run: `./install.sh`
4. Open a new terminal and you're ready to use Sansam!

## Usage

After installation, you can run Sansam programs directly using the `sansam` command:

```bash
sansam yourprogram.sans
```

No Python installation is required - Sansam runs as a standalone executable!

## Language Features

Sansam supports various programming constructs with Sanskrit keywords:

- Variables and basic data types
- Control structures (conditionals and loops)
- Functions
- Lists and Dictionaries
- Input/Output operations

## Basic Examples

### 1. Hello World
```sanskrit
मुद्रणः("नमस्ते विश्वम्")
```

### 2. Variables and Arithmetic
```sanskrit
क = 10
ख = 20
योग = क + ख
मुद्रणः(योग)  # Prints 30
```

### 3. Conditional Statements
```sanskrit
संख्या = 10
यदि संख्या > 5 {
    मुद्रणः("संख्या पञ्च अधिकः अस्ति")
} चेत् {
    मुद्रणः("संख्या पञ्च न्यूनः अस्ति")
}
```

### 4. Functions
```sanskrit
कार्य योगः(क, ख) {
    यच्छ क + ख
}

फल = योगः(5, 3)
मुद्रणः(फल)  # Prints 8
```

### 5. Lists
```sanskrit
सूची = [१, २, ३, ४, ५]
संकलः(सूची, ६)  # Append 6 to the list
मुद्रणः(सूची)   # Prints [1, 2, 3, 4, 5, 6]
```

## Built-in Functions

- `मुद्रणः()` - Print to console
- `आगम्()` - Get input from user
- `आगम्_पूर्णाङ्कः()` - Get integer input
- `किम्_पूर्णाङ्क()` - Check if value is number
- `किम्_सूत्र()` - Check if value is string
- `किम्_आवलि()` - Check if value is list
- `किम्_कार्य()` - Check if value is function

## File Extension

Sansam programs should use the `.sans` file extension. The interpreter will only execute files with this extension.

## Error Handling

The language provides clear error messages in case of syntax errors or runtime errors, making it easier to debug your programs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions and support, please open an issue in the GitHub repository.
