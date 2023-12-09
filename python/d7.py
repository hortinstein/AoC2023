import collections
from termcolor import colored

#read input file
f = open("../src/d7/p1input", "r")

order = ['A','K','Q','J','T','9','8','7','6','5','4','3','2'].reverse()

#       ['Z','Y','X',W',V"]
def eval_hand(hand):
    card_freqs = {x:hand.count(x) for x in hand}
    # Five of a kind, where all five cards have the same label: AAAAA
    if 5 in card_freqs.values():
        return 6,"Five of a kind"
    # Four of a kind, where four cards have the same label and one card has
    # a different label: AA8AA
    if 4 in card_freqs.values():
        return 5,"Four of a kind"
    # Full house, where three cards have the same label, and the remaining
    # two cards share a different label: 23332
    if 3 in card_freqs.values() and 2 in card_freqs.values():
       return 4,"Full house"
    # Three of a kind, where three cards have the same label, and the remaining
    # two cards are each different from any other card in the hand: TTT98
    if 3 in card_freqs.values():
        return 3, "Three of a kind"
    # Two pair, where two cards share one label, two other cards share a second
    # label, and the remaining card has a third label: 23432
    card_freq_list = list(card_freqs.values())
    if 2 in [card_freq_list.count(x) for x in card_freq_list]:
        return 2, "Two Pair"
    # One pair, where two cards share one label, and the other three cards have
    # a different label from the pair and each other: A23A4
    if 2 in card_freqs.values():
        return 1, "One Pair"
    # High card, where all cards' labels are distinct: 23456   
    return 0, "High Card"

def rank_hands(hands):
    return hands.sorted()

def sub_hands(hand):
    sub = "ZYXWV"
    unsub = "AQKJT"
    ret_hand = ""
    for card in hand:
        if card in unsub: ret_hand = ret_hand + sub[unsub.index(card)]
        elif card in sub: ret_hand = ret_hand + unsub[sub.index(card)]
        else: ret_hand = ret_hand + card
    return str(ret_hand)

hands = []
hand_bids = {}
for line in f:
    hand,bid = line.strip().split(" ")
    hand_bids[hand] = int(bid)

    #subs the cards for sorting
    hand = sub_hands(hand)

    hands.append(hand)

#replace with values so sort will work
sorted_hands = sorted(hands)
assert len(set(hands))==len(hands),"there is a duplicate hand in the list,need to handle edge case"

overall_rank = []

for hand in hands:
    #unsubs the cards for sorting
    rank = sorted_hands.index(hand)
    hand = sub_hands(hand)
    print (hand)
    score,hand_eval= eval_hand(hand)
    print ("hand: ",hand," bid: ",bid," points: ",score,rank," type: ",hand_eval)

    overall_rank.append((score,rank,hand,hand_bids[hand]))
overall_rank = sorted(overall_rank)
total_winnings = 0

for i,hand in enumerate(overall_rank):
    total_winnings+=(i+1)*hand[3]
    print (hand,":" ,i+1,"*",hand[3])
print (total_winnings)
