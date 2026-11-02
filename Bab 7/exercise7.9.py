
sandwich_orders = ['tuna', 'pastrami', 'ham', 'cheese', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print("Sorry, we are out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} sandwich.")