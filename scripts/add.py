#!/usr/bin/env python3
"""Simple addition utility."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=float, help="first number")
    parser.add_argument("b", type=float, help="second number")
    args = parser.parse_args()
    print(add(args.a, args.b))


if __name__ == "__main__":
    main()
