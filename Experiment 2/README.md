# Experiment 2

## Aim

To implement and understand the SHA-256 hashing algorithm for generating hash values and verifying the integrity of files by detecting modifications.

## SHA-256 Hashing

SHA-256 is a cryptographic hashing algorithm that generates a fixed-length 256-bit hash value for the given input.

A small change in the file content produces a different hash value, which can be used to detect file modification.

## File Integrity

File integrity is verified by generating the original SHA-256 hash and comparing it with the current hash of the file.

- Same hash → File is unmodified
- Different hash → File is modified

## Improvements

### Multiple File Integrity Checker

The program was extended to check multiple files in a single execution and report whether each file is modified or unmodified.

### Automatic Change-Location Detection

For modified text files, the program compares the original and current contents line-by-line and displays the changed line along with the original and current content.

## Files

- Experiment 2 Improved.py
- simple.txt
- notes.txt
- test.txt
- Output/

## Language Used

Python

## Library Used

hashlib

## Algorithm Used

SHA-256
