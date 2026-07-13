import random
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

yourcard = [] 
yourcard.append(deal_card())
yourcard.append(deal_card())

computercard = []
computercard.append(deal_card())

print(f"Your cards: {yourcard}, current score: {sum(yourcard)}")
print(f"Computer's first card: {computercard[0]}")

choice = input("Type 'y' to get another card, type 'n' to pass: ")
while choice == 'y':
    yourcard.append(deal_card())
    print(f"Your cards: {yourcard}, current score: {sum(yourcard)}")
    if sum(yourcard) > 21:
        print("You went over. You lose 😭")
        break
    choice = input("Type 'y' to get another card, type 'n' to pass: ")

if sum(yourcard) <= 21:
    computercard.append(deal_card())
    while sum(computercard) < 17:
        computercard.append(deal_card())

print(f"Your final hand: {yourcard}, final score: {sum(yourcard)}")
print(f"Computer's final hand: {computercard}, final score: {sum(computercard)}")

if sum(yourcard) > 21:
    print("You went over. You lose 😭") 
else:
    if sum(computercard) > 21:
        print("Computer went over. You win 😄")
    elif sum(yourcard) > sum(computercard):
        print("You win 😄")
    elif sum(yourcard) == sum(computercard):
        print("It's a draw!")
    else:
        print("You lose 😭")