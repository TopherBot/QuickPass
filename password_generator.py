#!/usr/bin/env python3
"""QuickPass – tiny password generator.
Generates a random password containing letters, digits, and punctuation.
Usage: python password_generator.py [length]
"""
import sys, string, secrets

def generate(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    except ValueError:
        print("Length must be an integer.", file=sys.stderr)
        sys.exit(1)
    print(generate(length))