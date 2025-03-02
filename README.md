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

## Running the program
First, clone the repository and navigate into the project directory:
```
git clone https://github.com/dk872/quadratic-solver
```
```
cd quadratic-solver
```

- **On Linux:**
  - Make sure you have Python installed. You can check with:
    ```
    python3 --version
    ```
  - Run the script and enter coefficients *manually*:
    ```
    python3 main.py
    ```
  - Or run the program *with the file* as an argument:
    ```
    python3 main.py <path-to-the-file>
    ```
  - Alternatively, make the script executable and run it directly:
    ```
    chmod +x main.py
    ./main.py
    ```

- **On Windows:**
  - Make sure Python is installed and added to the system PATH. You can check with:
    ```
    python --version
    ```
  - Run the script and enter coefficients *manually*:
    ```
    python main.py
    ```
  - Or run the program *with the file* as an argument:
    ```
    python main.py <path-to-the-file>
    ```

## Revert commit
[link](https://github.com/dk872/quadratic-solver/commit/c17bd9bdf7c6d255f560be94b62588c9fea8fc0a)