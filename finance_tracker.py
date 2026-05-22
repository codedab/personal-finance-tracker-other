import pandas as pd

data = pd.read_csv("transactions.csv")

food = 0
transport = 0
other = 0

for i in range(len(data)):
    if data["description"][i] == "food":
        food = food + data["amount"][i]
    elif data["description"][i] == "transport":
        transport = transport + data["amount"][i]
    else:
        other = other + data["amount"][i]

print("food: " + str(food))
print("transport: " + str(transport))
print("other: " + str(other))