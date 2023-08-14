import numpy as np
import sympy as sp
import re

# Function to perform Gaussian elimination on a matrix
def gaussian_elimination(matrix):
    rows, cols = matrix.shape
    for pivot_row in range(min(rows, cols - 1)):
        # Find the maximum absolute value in the column and swap rows
        max_row = np.argmax(np.abs(matrix[pivot_row:, pivot_row])) + pivot_row
        matrix[[pivot_row, max_row]] = matrix[[max_row, pivot_row]]

        # Normalize the pivot row
        pivot_value = matrix[pivot_row, pivot_row]
        matrix[pivot_row] /= pivot_value

        # Eliminate non-zero values below the pivot
        for row in range(pivot_row + 1, rows):
            factor = matrix[row, pivot_row]
            matrix[row] -= factor * matrix[pivot_row]

    return matrix

# Function to convert a matrix to echelon form
def convert_to_echelon_form(matrix):
    return gaussian_elimination(matrix)

def main():
    while True:
        try:
            # Get the number of equations from the user
            num_equations = int(input("Enter the number of equations: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Enter your equations or matrix (one equation/matrix entry per line):")
    equations = []
    equation_vars = set()

    # Input and preprocess equations
    for _ in range(num_equations):
        equation_str = input("Equation {}: ".format(_ + 1))
        equation_str = equation_str.replace(' ', '')

        # Insert multiplication operators before variables
        equation_str = re.sub(r'([0-9])([a-zA-Z])', r'\1*\2', equation_str)
        equation_str = re.sub(r'([a-zA-Z])([0-9])', r'\1*\2', equation_str)

        equation_terms = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+|\w+', equation_str)
        equation_vars |= set(term for term in equation_terms if term.isalpha())

        equations.append(equation_str)

    variables = sorted([str(var) for var in equation_vars])  # Ensure consistent variable order
    symbols = sp.symbols(' '.join(variables))

    eqns = []
    for equation in equations:
        try:
            lhs, rhs = equation.split('=')
            eqns.append(sp.Eq(sp.sympify(lhs), sp.sympify(rhs)))
        except (ValueError, SyntaxError) as e:
            print("Error processing equation:", equation)
            print("Error:", e)
            return

    try:
        # Convert equations to coefficient matrix and constants vector
        coef_matrix, constants = sp.linear_eq_to_matrix(eqns, symbols)
    except ValueError as e:
        print("Error creating coefficient matrix and constants vector.")
        print("Error:", e)
        return

    var_symbol_dict = {var: symbol for var, symbol in zip(variables, symbols)}

    coef_matrix = coef_matrix.subs(var_symbol_dict)
    constants = constants.subs(var_symbol_dict)

    augmented_matrix = np.hstack((coef_matrix, np.array(constants).reshape(-1, 1)))

    try:
        # Convert the matrix to echelon form using Gaussian elimination
        echelon_matrix = convert_to_echelon_form(augmented_matrix)
    except Exception as e:
        print("Error during Gaussian elimination.")
        print("Error:", e)
        return

    print("Echelon form:")
    print(echelon_matrix)

if __name__ == "__main__":
    main()
