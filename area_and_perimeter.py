#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on February 2022
# This is a file that lets you enter Length and Width to find the area and perimeter of a rectangle

import math


def main():
    # The Function Calculates Area and Perimeter

    # Input
    length_of_rectangle = int(input("Enter The Desired Length (mm): "))
    width_of_rectangle = int(input("Enter The Desired Width (mm): "))

    # Processing
    area = length_of_rectangle * width_of_rectangle
    perimeter = 2 * (length_of_rectangle + width_of_rectangle)

    # Output
    print("")
    print("Area is {0} mm².".format(area))
    print("Perimeter is {0} mm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
