import art

print(art.logo)
entry = True
bidders = {}
while entry:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    count = input("Are there any other bidders? Type 'yes or 'no'.\n")

    if count.lower() == "no":
        entry = False
    else:
        print("\n"*100)

great = 0
for key in bidders:
    if bidders[key] > great:
        great = bidders[key]
        names = []
        names.append(key)

final_names = "".join(names)
print(f"The winner is {final_names} with a bid of ${great}")