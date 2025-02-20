import sys


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
