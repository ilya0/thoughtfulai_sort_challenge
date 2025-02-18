# Package Sorting System

## Overview

This project implements a package sorting function for a robotic arm in Thoughtful’s automation factory. The function determines where to dispatch packages based on their **volume** and **mass** according to predefined rules.

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
│── tests.py          # Unit tests to validate sorting logic
```

## How to Use

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/package-sorting.git
   ```
2. Navigate to the project directory:
   ```sh
   cd package-sorting
   ```
3. Run the sorting function inside `sort.py` with test inputs:
   ```python
   from sort import sort

   print(sort(100, 50, 20, 10))  # Example usage
   ```

## Running Tests

To ensure the function works correctly, run the tests:

```sh
python tests.py
```

## Notes

- The function does **not** use a ternary operator, as per the project requirements.
- If you'd like to modify sorting criteria, update the `sort.py` logic.

