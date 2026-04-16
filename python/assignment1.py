
# Customer data
customers = [
    {"name": "Ravi", "payment": "UPI", "quantity": 2, "category": "electronics"},
    {"name": "Sita", "payment": "Card", "quantity": 1, "category": "clothing"},
    {"name": "Arjun", "payment": "UPI", "quantity": 1, "category": "books"},
    {"name": "Meena", "payment": "Cash", "quantity": 3, "category": "electronics"},
    {"name": "Rahul", "payment": "UPI", "quantity": 4, "category": "clothing"}
]

i = 0

print("Customers using UPI payment:")
while i < len(customers):
    if customers[i]["payment"] == "UPI":
        print(customers[i]["name"])
    i += 1

i = 0
print("Customers purchasing quantity more than 1:")
while i < len(customers):
    if customers[i]["quantity"] > 1:
        print(customers[i]["name"])
    i += 1

i = 0
print("Customers purchasing other than electronics category:")
while i < len(customers):
    if customers[i]["category"] != "electronics":
        print(customers[i]["name"])
    i += 1