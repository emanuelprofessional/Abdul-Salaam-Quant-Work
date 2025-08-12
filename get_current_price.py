import yfinance as yf
import argparse

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def get_price(metal):
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
    return metal_price





def main():
    parser = argparse.ArgumentParser(description="Get the price of a certain metal.")
    parser.add_argument("metal", choices = ["gold", "silver", "platinum"], help="The type of metal (gold, silver, platinum)")
    
    args = parser.parse_args()
    try:
        price = get_price(args.metal)
        print(f"\nThe price of {GREEN}${args.metal.lower()}{RESET} is {RED}${price:.2f}{RESET}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()