
nums = list(range(1, 10))
print(nums)

ending = ""
for num in nums:
    
    if num == 1:
        ending = "st"
    elif num == 2:
        ending = "nd"
    elif num == 3:
        ending = "rd"
    else:
        ending = "th"
    print(f"{num}{ending}")