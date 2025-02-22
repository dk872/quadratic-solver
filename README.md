# Quadratic Equation Solver  

## Description
This program solves quadratic equations of the form *ax² + bx + c = 0*. 
It calculates the roots of the equation using the quadratic formula and handles 
different cases based on the discriminant. The coefficients can be entered manually 
or read from a file.  

## Input requirements
- **When entering coefficients manually**:  
  - The program prompts for `a`, `b`, and `c`.  
  - The input must be a valid real number.  
  - `a` cannot be `0`, as it would make the equation linear (this applies to all input formats).

- **When reading from a file**:  
  - The file must contain exactly three space-separated numbers on a single line.
  - The decimal separator must be a dot `.` . 
  - The file must end with a newline character `\n` after the last coefficient (c).
  - Example of a valid file content:  
    ```
    1.0 -3.0 2.0
    ```