from termcolor import colored
from tqdm import tqdm

rm_blnks = lambda n: [i for i in n if i]
cast_ints = lambda n: [int(i) for i in n ]

#read input file
f = open("../src/d5/p1input", "r")

almanac = f.read().split("\n\n")
seeds = rm_blnks(almanac[0].split(":")[1].split(" "))

almanac_parsed = {"seeds":cast_ints(seeds)}
ordered_name = []
for entry in almanac[1:]:
    name,ranges = entry.split(" map:")
    almanac_parsed[name] = []
    # print (name)
    ordered_name.append(name)
    for ranges in rm_blnks(ranges.strip().split("\n")):
        # splits each into three parts:
        destination_range_start,source_range_start,range_length = cast_ints(ranges.split(" "))
        
        
        destination_range = range(destination_range_start,destination_range_start+range_length)
        source_range = range (source_range_start,source_range_start+range_length)
        almanac_parsed[name].append((source_range,destination_range))        
        
        # print ("dest:", destination_range,"src",source_range)
    almanac_parsed[name] = sorted(almanac_parsed[name], key=lambda x: x[0].start)


def find_locations(seeds,ordered_name,almanac_parsed):
    #results = []
    lowest = 2**32
    for seed in tqdm(seeds):
        # print (seed,' ',end='')
        for name in ordered_name:
            # print(name)
            original = seed
            for src_dest_range in almanac_parsed[name]:
                #if its in the source
                if seed in src_dest_range[0]:
                    seed_src = src_dest_range[0].index(seed)
                    seed = src_dest_range[1][seed_src]
                    # print (name,' -> ',colored(seed,"green"),' ', end='')
                    break
            # if original == seed:
            #     # print (name,' -> ',colored(seed,"red"),' ', end='')
        # print (colored('END',"yellow"))
        if seed < lowest: lowest = seed 
        #results.append(seed)
    #results = sorted(results)
    print (colored('Lowest',"yellow"),lowest)#,results[0])
    
find_locations(almanac_parsed["seeds"],ordered_name,almanac_parsed)

#almanac_parsed = {"seeds": [0, 5, 10, 3]}  # Example data
new_seeds = []
for i in tqdm(range(0, len(almanac_parsed["seeds"]), 2)):
    start = almanac_parsed["seeds"][i]
    range_len = almanac_parsed["seeds"][i+1]

    new_seeds.extend(list(range(start,start+range_len)))

# print(new_seeds)
# Flatten the list of lists
find_locations(new_seeds,ordered_name,almanac_parsed)
