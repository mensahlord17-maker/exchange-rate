# importing the requests library to make API calls to the exchange rate API, and defining the API key and base URL for the API.
import requests

API_KEY = "638f842f4c35de2b16cce804"
BASE_URL = "https://v6.exchangerate-api.com/v6"


# Function to get the exchange rate between two currencies
def get_rate(base, target):
    url = f"{BASE_URL}/{API_KEY}/latest/{base}"
    response = requests.get(url)
    data = response.json()

    try:
        rate = data["conversion_rates"][target]
        return rate
    except KeyError:
        print(f"Could not find rate for {target}")
        return None


# Function to display the results of the exchange rate calculation
def display_results(amount, base, target, rate):
    result = amount * rate
    print(f"{amount} {base} = {result:.2f} {target}")


# Function to run the main program loop, allowing the user to input currencies and amounts, and displaying the results until they choose to quit.
def main():
    while True:
        base = input("enter base currency or 'q' to quit: ")
        if base.lower() == "q":
            print("Exiting the program.")
            break
        target = input("enter the target currency ")
        amount = float(input("enter amount "))
        data = get_rate(base, target)
        if data:
            display_results(amount, base, target, data)


main()
