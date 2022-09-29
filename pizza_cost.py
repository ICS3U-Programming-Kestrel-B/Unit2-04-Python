#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Sep. 29, 2022
# This program calculates the cost
# of a pizza with diameter


import constants


def main():
    # input
    print("This program calculates the")
    print("cost of a pizza with diameter.")
    print("")
    diameter = int(input("Enter the pizza's diameter in inches: "))

    # process
    # subtotal = 2 + 2.25 + 1.5 * diameter
    subtotal = (
        constants.LABOUR_COST
        + constants.RENT_COST
        + constants.INGREDIENT_COST * diameter
    )
    # tax = subtotal * 0.13
    tax = subtotal * constants.HST
    total = tax + subtotal

    # output
    print("")
    print("Your total is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
