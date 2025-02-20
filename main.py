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