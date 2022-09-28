#!/usr/bin/python3


def count(currency_dict):
    total = 0.0
    income = 0.0

    total += currency_dict["quarters"] * 0.25
    total += currency_dict["dimes"] * 0.10
    total += currency_dict["nickels"] * 0.05
    total += currency_dict["pennies"] * 0.01
    
    total += currency_dict["rolls"]

    total += currency_dict["twenties"] * 20.00
    total += currency_dict["tens"] * 10.00
    total += currency_dict["fives"] * 5.00
    total += currency_dict["ones"] * 1.00

    total += currency_dict["slips"]

    income = total - currency_dict["drawer_hold"]
    off = income - currency_dict["expected_in"]

    return(total, income, off)

def retrieve_drawer():
    currency_dict = {}

    currency_dict["quarters"] = int(input("\n\nQuarters: "))
    currency_dict["dimes"] = int(input("Dimes: "))
    currency_dict["nickels"] = int(input("Nickels: "))
    currency_dict["pennies"] = int(input("Pennies: "))

    currency_dict["rolls"] = float(input("\nRolls: "))

    currency_dict["twenties"] = int(input("\nTwenties: "))
    currency_dict["tens"] = int(input("Tens: "))
    currency_dict["fives"] = int(input("Fives: "))
    currency_dict["ones"] = int(input("Ones: "))

    currency_dict["slips"] = float(input("\nSlips: "))

    currency_dict["drawer_hold"] = float(input("\nDrawer Hold: "))
    currency_dict["expected_in"] = float(input("Expected Income: "))

    return(currency_dict)

def drawer_reciept(total, income, off, currency_dict):
    print("\n\n==========================\n")
    print("Total: " + format(total, '.2f'))
    print("\nIncome: " + format(income, '.2f'))
    print("Expected: " + format(currency_dict["expected_in"], '.2f'))
    print("Offset: " + format(off, '.2f'))
    print("\n==========================\n\n")


if __name__ == "__main__":
    currency_dict = retrieve_drawer()
    total,income,off = count(currency_dict)

    drawer_reciept(total, income, off, currency_dict)
