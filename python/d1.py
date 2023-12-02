numSpelledOutDict = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
  "zero": "0"
}

numSpelledOutArray = [
    "one","1",
    "two", "2",
    "three", "3",
    "four","4",
    "five", "5",
    "six","6",
    "seven", "7",
    "eight", "8",
    "nine", "9",
    "zero", "0"
]

#read input file
f = open("../src/d1/p1input", "r")
total = 0
for line in f: 
  print (line)
  found_nums = []
  for i,c in enumerate(line):
    if c in numSpelledOutArray:
      found_nums.append(c)
    else:  
      for k,v in numSpelledOutDict.items():
        # print(k,v,line[i:(i+len(k))])
        if k == line[i:(i+len(k))]:
          found_nums.append(v)
        
  print (found_nums)
  number = str(found_nums[0]) + str(found_nums[-1])
  print(number)
  total += int(number)
print (total)