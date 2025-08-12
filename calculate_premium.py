import numpy as np
import yfinance as yf
import argparse
import math

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def calc_premium(metal, dollar_amount, amount_of_metal, unit):
    if metal.lower() == "gold":
        ticker = "GC=F"
    elif metal.lower() == "silver":
        ticker = "SI=F"
    elif metal.lower() == "platinum":
        ticker = "PL=F"
    else:
        raise ValueError("Unsupported metal. Please choose gold, silver, or platinum.")
    
    metal_data = yf.Ticker(ticker)
    metal_price = metal_data.history(period="1d")['Close'].iloc[-1]
    if unit.lower() == "kg":
        factor = 35.274
    elif unit.lower() == "g":
        factor = 0.0321507
    else:
        factor = 1.0
    demoninator = metal_price * factor * amount_of_metal
    premium_price = ((dollar_amount / demoninator) - 1) * 100
    premium_price = math.trunc(premium_price * 100) / 100
    return f"{premium_price}%"


def main():
    parser = argparse.ArgumentParser(description="Get the value of a specified amount of metal.")
    parser.add_argument("metal", choices = ["gold", "silver", "platinum"], help="The type of metal (gold, silver, platinum)")
    parser.add_argument("dollars", type=float, help="The dollar amount of the selected metal in ounces (e.g., 25.67, .25, 1000, etc)")
    parser.add_argument("amount_of_metal", type=float, help="The amount of metal (e.g., 1, .25, 20, etc)")
    parser.add_argument("unit", choices=["oz", "kg", "g"], help="The metric of the metal (oz, kg, g)")
    
    args = parser.parse_args()
    try:
        premium = calc_premium(args.metal, args.dollars, args.amount_of_metal, args.unit)
        print(f"\nThe premium for {GREEN}${args.dollars:.2f}{RESET} associating with {GREEN}{args.amount_of_metal} {args.unit}{RESET} of {GREEN}{args.metal.lower()}{RESET} is: {RED}{premium}{RESET}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()