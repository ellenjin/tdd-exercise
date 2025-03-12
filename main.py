VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    face_cards = ['Jack', 'Queen', 'King']
    total_sum = 0
    aces_count = 0

    if len(hand) > 5:
        return "Invalid"
    
    for card in hand:
        if not card in VALID_CARDS: 
            print(f"Invalid card: {card}")
            return "Invalid"
        
        if card == 'Ace':
            aces_count += 1
        elif card in face_cards:
            total_sum += 10
        else: 
            total_sum += card
        
    while aces_count > 0:
        if total_sum > 10 or (aces_count > 1 and total_sum == 10):
            total_sum += 1
        else: 
            total_sum += 11

        aces_count -= 1
        
    if total_sum > 21:
        return "Bust"
        
    return total_sum