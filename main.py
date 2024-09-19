# Created by John Fiore
# 09-19-2024 @ 11:45

import ts_stocks

price = ts_stocks.get_current_price()
prediction = ts_stocks.get_future_price()

print("Today, the stock price is $" + str(price))
print("Our prediction: in one week, it will be worth $" + str(prediction))

if prediction > price:
    print("Alright, good investment!")
elif prediction == price:
    print("Eh, it's OK.")
else:
    print("This is awful...")
