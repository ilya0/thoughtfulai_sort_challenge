# Package Sorting System

## Overview

This project implements a package sorting function for a robotic arm. The function determines where to dispatch packages based on their **volume** and **mass** according to predefined rules.

## Sorting Rules

Packages are categorized as follows:

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy but not both.
- **REJECTED**: Packages that are both bulky and heavy.

### Definitions:
- A package is **bulky** if:
  - Its **volume** (Width × Height × Length) is **≥ 1,000,000 cm³**, OR
  - Any single dimension is **≥ 150 cm**.
- A package is **heavy** if its **mass** is **≥ 20 kg**.

## File Structure

```
/package-sorting
│── README.md         # Project documentation
│── sort.py           # Python function that classifies packages
│── pseudocode.py     # High-level breakdown of the logic

```

## How to Use

1. Clone the repository:
   ```sh
   git clone 
   ```

2. Run `sort.py` 


## Notes

- The function does **not** use a ternary operator, as per the project requirements.
- If you'd like to modify sorting criteria, update the `sort.py` logic.

