#read input file
f = open("../src/d9/p1input", "r")

cast_ints = lambda n: [int(i) for i in n ]
total = 0
for line in f:
    nums = cast_ints(line.split(" "))
    ends = [nums[-1]]
    aggregated_differences = []
    differences = []
    print (nums)
    while 1:
        if differences != [] and all(x == 0 for x in differences): break
        differences = []
        for i in range(len(nums) - 1):
            difference = nums[i+1] - nums[i]
            differences.append(difference)
        ends.append(differences[-1])
        aggregated_differences.append(differences)
        nums = differences
        print (differences)
    total+=sum(ends)
    print (sum(ends))


    for i,difference in enumerate(aggregated_differences.reverse())
        next_num = [aggregated_differences[i]]
print (total)

