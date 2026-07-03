# GC-Content-Classifier
Python program to calculate and classify GC content from DNA FASTA sequences.
# GC Content Classifier

## Overview

This project is a Python program that reads DNA sequences from a FASTA file, calculates the GC content of each gene using the Biopython library, and classifies each gene based on its GC percentage.

## Features

- Reads DNA sequences from a FASTA file
- Calculates GC content using `gc_fraction()` from Biopython
- Classifies genes into:
  - LOW GC CONTENT (<40%)
  - MEDIUM GC CONTENT (40–60%)
  - HIGH GC CONTENT (>60%)
- Writes the results to an output text file

## Technologies Used

- Python 3
- Biopython

## Installation

Install Biopython before running the program:

```bash
pip install biopython
```

## Input File

The program reads DNA sequences from a FASTA file named **gene.fa**.

Example:

```text
>GeneA
ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC
>GeneB
ATATATATATATATATATATATATATATATATATATATATATATA
>GeneC
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
```

## Output

The program generates a file named **gc_classification.txt** containing:

- Gene name
- GC percentage
- GC content classification

Example format:

```text
GeneA    51.1    MEDIUM GC CONTENT
GeneB     0.0    LOW GC CONTENT
GeneC   100.0    HIGH GC CONTENT
```

## How to Run

Run the program using:

```bash
python gc_classifier.py
```

## Project Structure

```text
GC-Content-Classifier/
│
├── gc_classifier.py
├── gene.fa
├── gc_classification.txt
└── README.md
```

## Learning Objectives

This project demonstrates:

- Reading FASTA files
- String manipulation in Python
- File input/output
- Using the Biopython library
- Calculating GC content
- Writing formatted output files

## Author

**Riddhima Mishra**

Bioinformatics student learning Python and computational biology.
