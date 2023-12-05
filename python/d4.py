from termcolor import colored

#read input file
f = open("../src/d4/p1input", "r")

def double_number_n_times(n):
    result = 1
    for i in range(n):
        result *= 2
    return result
total = 0


card_totals = {}

for line in f:
    print (line)
    card_num,nums = line.split(":")
    # removing duplicate spaces then getting the number
    card_num = int(" ".join(card_num.split()).split(' ')[1])
    winners,players = nums.split("|")
    winners = [x.strip(' \n') for x in winners[1:-1].split(" ")]
    players = [x.strip(' \n') for x in players[1:].split(" ")]

    # using list comprehension to perform removal of empty strings
    winners = [i for i in winners if i]
    players = [i for i in players if i]
    common_list = [c for c in winners if c in players]

    double_increment = lambda n: 2 ** (n - 1) if n > 0 else 0
    score = double_increment(len(common_list))
    total+=score
    print (colored(card_num,'red'),winners,players,common_list,colored(score,'green'))
    card_totals[card_num] = len(common_list)

copies = {}
for key in card_totals:
    copies[key] = 1

print(colored(total,'yellow'))
print(colored(card_totals,'yellow'))
