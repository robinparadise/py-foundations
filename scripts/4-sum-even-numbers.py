price = 19.99
tax_rate = 0.08
total = price * (1 + tax_rate)

def twoDecimals(valor):
  return round(valor, 2)

message = f"The total cost is ${twoDecimals(total)}."
print(message)
