# Equation Solver

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Input Formats](#input-formats)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Overview

The `equation_solver.py` script is a Python program that facilitates solving systems of linear equations using the Gaussian elimination method. It supports both regular equation formats and mixed variable naming formats. The script utilizes the `numpy` and `sympy` libraries to optimize matrix operations and perform symbolic mathematics.

## Prerequisites

To run the script, you'll need the following:

- Python 3.x
- NumPy library (`pip install numpy`)
- SymPy library (`pip install sympy`)

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing the `equation_solver.py` script.

3. Run the script using the following command:


4. Follow the prompts to input the number of equations and the equations themselves. Refer to the [Input Formats](#input-formats) section for proper input guidelines.

5. The script will process the input equations, perform Gaussian elimination, and display the echelon form of the augmented matrix.

## Input Formats

The script supports two equation formats:

- **Regular Equation Format**:
Example:
3x - 2y + z = 4


- **Mixed Variable Naming Format**:
Example:
x1 - 2x2 + x3 = 4


## Examples

Regular Equation Format:
Enter the number of equations: 3
Enter your equations or matrix (one equation/matrix entry per line):
Equation 1: 3x - 2y + z = 4
Equation 2: 2x + y - z = -1
Equation 3: x + 3y - 2z = 3


Mixed Variable Naming Format:
Enter the number of equations: 3
Enter your equations or matrix (one equation/matrix entry per line):
Equation 1: x1 - 2x2 + x3 = 4
Equation 2: 2x1 + x2 - x3 = -1
Equation 3: x1 + 3x2 - 2x3 = 3


## Troubleshooting

- If an error occurs during input parsing or matrix processing, the script will display an error message along with a description of the issue.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests on the [GitHub repository](https://github.com/darioblopes/equation_solver).


