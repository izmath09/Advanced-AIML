suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
sample_space_cards = [(rank, suit) for rank in ranks for suit in suits]
def calculate_probability(event, sample_space):
return len(event) / len(sample_space)
event_heart = [card for card in sample_space_cards if card[1] == "Hearts"]
event_ace = [card for card in sample_space_cards if card[0] == "A"]
event_red = [card for card in sample_space_cards if card[1] in ["Hearts", "Diamonds"]]
prob_heart = calculate_probability(event_heart, sample_space_cards)
prob_ace = calculate_probability(event_ace, sample_space_cards)
prob_red = calculate_probability(event_red, sample_space_cards)
# Manual table formatting
print("+--------------------------------------+----------------------+-------------+-------------+")
print("| Event | Favorable Outcomes | Total Cards| Probability|")
print("+--------------------------------------+----------------------+-------------+-------------+")
print(f"| Drawing a Heart | {len(event_heart):<21}| 52 |
{prob_heart:.2f} |")
print(f"| Drawing an Ace | {len(event_ace):<21}| 52 | {prob_ace:.2f} |")
print(f"| Drawing a Red card | {len(event_red):<21}| 52 | {prob_red:.2f} |")
print("+--------------------------------------+----------------------+-------------+-------------+")
