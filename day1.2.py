file = open("input1.1.txt")
nums = file.readlines()
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if(int(nums[i]) + int(nums[j]) + int(nums[k]) == 2020):
                print(int(nums[i])*int(nums[j])*int(nums[k]) )
            
file.close()
