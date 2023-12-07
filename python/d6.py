from termcolor import colored
from tqdm import tqdm
def parse_races(f,p2=False):
    #function that strips the new lines, checks to make sure it's not blank and casts to ints
    strip_rmblnks_cast = lambda n: [int(i) for i in n if i]
    lines = f.readlines()
    if not p2:
        times = strip_rmblnks_cast(lines[0].split(" ")[1:])
        record_distances = strip_rmblnks_cast(lines[1].split(" ")[1:])
        return times,record_distances
    time = int(lines[0].split(":")[1].replace(" ",''))
    record_distance = int(lines[1].split(":")[1].replace(" ",''))
    return [time],[record_distance]
def calc_wins(times,record_distances):
    answer = 1
    for i in range(len(times)):
        time = times[i]
        record = record_distances[i]
        print ("Race ",i,": ",times,"ms - Record:",record," millimeters")
        winners = []
        for i in tqdm(range(time+1)):
            held = i
            time_remaiming = time-i
            traveled = held *time_remaiming
            if traveled > record:
                # print (held,time_remaiming,colored(traveled,'green'))
                winners.append(held)
            # else:
            #     print (held,time_remaiming,colored(traveled,'red'))
        print (colored(len(winners),'yellow'))
        answer*=len(winners)
    print (colored(answer,'blue'))
    
#read input file
f = open("../src/d6/p1input", "r")

times, record_distances = parse_races(f)
calc_wins(times, record_distances)

#read input file
f = open("../src/d6/p1input", "r")

times, record_distances = parse_races(f,p2=True)
calc_wins(times, record_distances)
