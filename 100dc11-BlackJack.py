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

burst = False
choice = input("Type 'y' to get another card, type 'n' to pass: ")
while choice == 'y':
    next_card = deal_card()
    if next_card == 11 and (11 in yourcard) and sum(yourcard) + 11 > 21:
        next_card = 1
    yourcard.append(next_card)
    print(f"Your cards: {yourcard}, current score: {sum(yourcard)}")
    if sum(yourcard) > 21:
        print("You went over. You lose 😭")
        burst = True
        break
    choice = input("Type 'y' to get another card, type 'n' to pass: ")

if sum(yourcard) <= 21:
    while sum(computercard) < 17:
        next_card = deal_card()
        if next_card == 11 and (11 in computercard) and sum(computercard) + 11 > 21:
            next_card = 1
        computercard.append(next_card)  
        
if burst == False:
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
        elif sum(yourcard) == 21 and sum(computercard) != 21:
            print("You win 😄")
        elif sum(computercard) == 21 and sum(yourcard) != 21:
            print("You lose 😭")        
        else:
            print("You lose 😭")