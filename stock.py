stocks = {
    "INFY": 1500,
    "TCS": 3500,
    "WIPRO": 500
}
total_investment = 0
print("Stock Portfolio Tracker")
print("-----------------------")
for stock, price in stocks.items():
    quantity = int(input("Enter quantity for " + stock + ": "))
    investment = price * quantity
    total_investment += investment
    print(stock, "Investment =", investment)
print("-----------------------")
print("Total Investment Value =", total_investment)