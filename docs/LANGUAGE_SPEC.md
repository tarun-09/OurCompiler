# Sansam Language Specification

## Table of Contents
1. [Introduction](#introduction)
2. [Syntax Overview](#syntax-overview)
3. [Language Elements](#language-elements)
4. [Control Structures](#control-structures)
5. [Functions](#functions)
6. [Data Types](#data-types)
7. [Operators](#operators)
8. [Built-in Functions](#built-in-functions)

## Introduction

Sansam is a Sanskrit-based programming language that combines the elegance of Sanskrit with modern programming concepts. The language uses Devanagari script for keywords while maintaining familiar programming structures.

## Syntax Overview

Programs in Sansam are written using a combination of Sanskrit keywords and standard programming constructs. The syntax emphasizes readability and maintains familiarity with common programming patterns.

## Language Elements

### Keywords
- `यच्छ` (yachCha) - Return statement
- `विघ्नः` (vighnaH) - Break statement
- `अनुवर्तते` (anuvartate) - Continue statement
- `यदि` (yadi) - If statement
- `नोचेत्` (nochet) - Else if
- `चेत्` (chet) - Else
- `यावद्` (yavad) - While loop
- `प्रति` (prati) - For loop
- `कार्य` (kaarya) - Function definition
- `वा` (vaa) - OR operator
- `च` (cha) - AND operator
- `न` (na) - NOT operator

### Variables
Variables are dynamically typed and can be assigned using the `=` operator:
```sanskrit
क = 5        # Integer assignment
नाम = "राम"  # String assignment
```

## Control Structures

### If-Else Statements
```sanskrit
यदि क > 5 {
    मुद्रणः("बृहत्")
} नोचेत् क < 0 {
    मुद्रणः("ऋणम्")
} चेत् {
    मुद्रणः("मध्यम्")
}
```

### While Loops
```sanskrit
यावद् क > 0 {
    मुद्रणः(क)
    क = क - 1
}
```

### For Loops
```sanskrit
प्रति क इन सूची {
    मुद्रणः(क)
}
```

## Functions

Functions are defined using the `कार्य` keyword:
```sanskrit
कार्य योगः(क, ख) {
    यच्छ क + ख
}
```

## Data Types

1. Numbers
   - Integers: `१`, `२`, `३`, etc.
   - Floats: `१.५`, `२.०`, etc.

2. Strings
   ```sanskrit
   नाम = "श्री राम"
   ```

3. Lists
   ```sanskrit
   सूची = [1, 2, 3, 4, 5]
   ```

4. Dictionaries
   ```sanskrit
   कोश = {क: "का", ख: "खा"}
   ```

5. Booleans
   - `सत्यम्` (True)
   - `असत्यम्` (False)

## Operators

### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus
- `^` Power

### Comparison Operators
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

### Logical Operators
- `वा` (OR)
- `च` (AND)
- `न` (NOT)

### Bitwise Operators
- `>>` Right shift
- `<<` Left shift
- `^` XOR

## Built-in Functions

1. `मुद्रणः()` - Print function
   ```sanskrit
   मुद्रणः("नमस्ते विश्वम्")
   ```

2. `आगम्()` - Input function
   ```sanskrit
   नाम = आगम्()
   ```

3. List Operations
   - `संकलः()` - Append
   - `पोप()` - Pop
   - `अतिसृ()` - Extend

4. Type Checking
   - `किम्_पूर्णाङ्क()` - Is number
   - `किम्_सूत्र()` - Is string
   - `किम्_आवलि()` - Is list
   - `किम्_कार्य()` - Is function
