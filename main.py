import sys
import math


def get_coefficient(name: str) -> float:
    while True:
        try:
            value = input(f"{name} = ")
            num = float(value)
            if name == "a" and num == 0:
                print("Error. a cannot be 0.", file=sys.stdout)
                continue
            return num
        except ValueError:
            print(f"Error. Expected a valid real number, got {value} instead", file=sys.stdout)


def read_coefficients_from_file(filename: str):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                print("invalid file format", file=sys.stdout)
                sys.exit(1)
            a, b, c = map(float, parts)
            if a == 0:
                print("Error. a cannot be 0", file=sys.stdout)
                sys.exit(1)
            return a, b, c
    except FileNotFoundError:
        print(f"file {filename} does not exist", file=sys.stdout)
        sys.exit(1)
    except ValueError:
        print("invalid file format", file=sys.stdout)
        sys.exit(1)


def solve_quadratic(a: float, b: float, c: float):
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {0.0 if root1 == -0.0 else root1}")
        print(f"x2 = {0.0 if root2 == -0.0 else root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print("There is 1 root")
        print(f"x1 = {0.0 if root == -0.0 else root}")
    else:
        print("There are 0 roots")


def main():
    if len(sys.argv) == 2:
        a, b, c = read_coefficients_from_file(sys.argv[1])
    else:
        a = get_coefficient("a")
        b = get_coefficient("b")
        c = get_coefficient("c")
    solve_quadratic(a, b, c)


if __name__ == "__main__":
    main()
    