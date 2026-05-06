# Exam 4_Karen Alldridge
# BIO 539
## Overview
This project implements a genome k-mer analysis tool written in python.  
DNA sequences are represented as strings containing the nucleotides: A, C, G, T

The program:
- extracts k-mers (substrings of length k)
- counts how often each k-mer appears
- records the frequency of the character that follows each k-mer
- outputs the results to a file

This is a model of techniques used in genome assembly. 

## Project Files
- `python_script.py` → main program
- `test_python_script.py` → pytest test suite (TDD approach)
- `README.md` → documentation

## How to run the program

Run from the command line:

```bash
python python_script.py <input_file> <k> <output_file>~

Example: python python_script.py sample_input.txt 3 results.txt

Parameters:
<input_file>: text file containing DNA sequences (one per line)
<k>: length of k-mers
<output_file>: file where results are saved

## How to run tests

Run from the command line:
```bash pytest
Expected output: collected 11 items; 11 passed
To see detailed outputs:
```bash pytest -v 

## Remember to add dataset files so the script can fully run.

## AI Statement:
I used AI to assist me with finding errors in the code (debugging) and correcting them accordingly. As I ran each portion of the script, I double checked it with ChatGPT and used it to assist me with writing the docstrings, I then added my comments throughout the script. 
I also used AI to assist me with creating my tests and adding more to cover more issues that may arise (ex. long/short strings, missing data, etc.).
It was increadibly helpful to have this tool to go back and forth with as I worked on the assignment and it assisted me with understanding how to write the script more clearly. 
