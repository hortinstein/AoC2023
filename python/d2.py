#read input file
f = open("../src/d2/p1input", "r")

max_cubes = {
  "red": 12,
  "blue": 14,
  "green": 13,
}


def validates_game(results,game_num):
  for x in results:
      num,color = x.split(" ")
      if color in max_cubes and int(num) > max_cubes[color]:
        # print("Too many " + color + " cubes in game " + game_num)
        return True
  return False  

def return_fewest_power(games):
  least_cubes = {
    "red": 0,
    "blue": 0,
    "green": 0,
  }
  # print (games)
  for game in games:
    results = [x.strip(' ') for x in game.split(",")]      
    for x in results:
      num,color = [x.strip(' \n') for x in x.split(" ")]
      if int(least_cubes[color]) < int(num):
        least_cubes[color] = int(num) 
  print ("least",least_cubes)
  total = 1
  for k,v in least_cubes.items():
    if v != 0:
      total *= v
  return total

def game_info(line):
  game_num = line.split(" ")[1][:-1]
  games = line.split(":")[1].split(";")
  return game_num, games
  

total = 0
total_power = 0

for line in f: 
  print (line)
  busted = False
  game_num, games = game_info(line)
  for game in games:
    results = [x.strip(' ') for x in game.split(",")]
    busted = validates_game(results,game_num)
    if busted: break
  if not busted:
    total+=int(game_num)
  power = return_fewest_power(games)
  print("power",power)
  total_power += power
    

print (total)
print (total_power)