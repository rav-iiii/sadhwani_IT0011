import csv

def read_exchange_rates(filename):
    exchange_data = {}
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for record in csv_reader:
            currency_code, currency_name, exchange_value = record
            exchange_data[currency_code.upper().strip()] = (currency_name.strip(), float(exchange_value))
    return exchange_data

def convert_currency():
    rate_info = read_exchange_rates('currency.csv')
    usd_amount = float(input("How much dollar do you have? "))
    desired_currency = input("What currency you want to have? ").upper().strip()

    if desired_currency in rate_info:
        currency_name, conversion_rate = rate_info[desired_currency]
        result = usd_amount * conversion_rate
        print(f"\nDollar: {usd_amount} USD")
        print(f"{currency_name}: {result}")
    else:
        print("Currency not found.")

if __name__ == "__main__":
    convert_currency()