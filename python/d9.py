#read input file
f = open("../src/d9/p1input", "r")

cast_ints = lambda n: [int(i) for i in n ]
total = 0
for line in f:
    nums = cast_ints(line.split(" "))
    differences = []
    while all(x != 0 for x in differences):
        differences = []
        for i in range(len(nums) - 1):
            difference = nums[i+1] - nums[i]
            differences.append(difference)
        print (differences)