# Genome Assembly as Shortest Superstring

## Overview
This project solves the **Genome Assembly as Shortest Superstring** problem, commonly encountered in bioinformatics. It reconstructs a chromosome from a collection of DNA reads by gluing overlapping pairs together to form the shortest possible superstring.

## Input
- A FASTA file containing at most 50 DNA strings.
- Each string is of approximately equal length (not exceeding 1000 base pairs).

The dataset satisfies the condition:
> There exists a unique way to reconstruct the chromosome by overlapping reads by more than half their length.

## Goal
Construct the **shortest superstring** that contains all reads.

## Key Concepts
- **Superstring**: A string containing all reads as substrings.
- **Overlap**: Suffix of one read matching prefix of another.
- **Parsimony**: Favoring the shortest valid superstring.

## Dependencies
- Python 3.x
- [Biopython](https://biopython.org/)

Install Biopython:
```bash
pip install biopython
```

## Usage
1. Prepare your input FASTA file as `input.txt`.
2. Run the script:

```bash
python genome_superstring.py
```

## Output
- Prints the shortest superstring to standard output.

## Files
- `genome_superstring.py`: Python script to solve the problem.
- `input.txt`: Input FASTA file containing DNA reads.

## Example
### Input (FASTA)
```
>Read1
ATTAGACCTG
>Read2
CCTGCCGGAA
>Read3
AGACCTGCCG
>Read4
GCCGGAATAC
```
### Output
```
ATTAGACCTGCCGGAATAC
```
