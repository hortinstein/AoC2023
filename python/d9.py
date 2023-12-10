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
        # print (differences)
    total+=sum(ends)
    print (sum(ends))
    aggregated_differences[-1].insert(0,0)
    #loop through backwards
    for i,difference in reversed(list(enumerate(aggregated_differences))):
        if i+1==len(aggregated_differences):
            continue
        print (i)
        next_num = aggregated_differences[i][0] - aggregated_differences[i+1][0]
        print ("next element",aggregated_differences[i][0],"-",aggregated_differences[i+1][0],"=",next_num)
        print (aggregated_differences[i+1])
        aggregated_differences[i].insert(next_num,0)
        print (aggregated_differences[i])
    print (aggregated_differences[0])
print (total)

