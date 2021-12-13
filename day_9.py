continues = True
bids = {}

print("This is a blind auction!")
while continues:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    decision = input("Write 'yes' if someone else wants to bid ")
    bids[name] = bid
    if decision != 'yes':
        continues = False

winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a ${bids[winner]}!")
