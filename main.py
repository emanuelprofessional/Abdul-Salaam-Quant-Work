import numpy as np
import pandas as pd
# import matplotlib as mp
import yfinance as yf
import argparse

def get_metal_price(metal, amount, unit):
    if metal.lower() == "gold":
        ticker = "GC=F"
    elif metal.lower() == "silver":
        ticker = "SI=F"
    elif metal.lower() == "platinum":
        ticker = "PL=F"
    else:
        raise ValueError("Unsupported metal. Please choose gold, silver, or platinum.")
    
    if unit.lower() == "kg":
        amount_in_oz = round(float(amount) * 35.274, 4)
    elif unit.lower() == "g":
        amount_in_oz = round(float(amount) / 28.3495, 4)
    else:
        amount_in_oz = amount
    
    metal_data = yf.Ticker(ticker)
    metal_price = metal_data.history(period="1d")['Close'].iloc[-1]
    total_value = round(metal_price * amount_in_oz, 2)
    return '$' + str(total_value)
    

def main():
    parser = argparse.ArgumentParser(description="Get the value of a specified amount of metal.")
    parser.add_argument("metal", choices = ["gold", "silver", "platinum"], help="The type of metal (gold, silver, platinum)")
    parser.add_argument("amount", type=float, help="The amount of metal (e.g., 1, .25, 20, etc)")
    parser.add_argument("unit", choices=["oz", "kg", "g"], help="The metric of the metal (oz, kg, g)")

    args = parser.parse_args()

    try:
        value = get_metal_price(args.metal, args.amount, args.unit)
        print(f"\nThe value of {args.amount} {args.unit.lower()} of {args.metal.lower()} is: {value}")
    except ValueError as e:
        print(e)










if __name__ == "__main__":
    main()