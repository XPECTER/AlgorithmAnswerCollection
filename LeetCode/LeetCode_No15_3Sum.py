def threeSum(nums):
    # #   brute force solution
    # answer = []
    #
    # for i in range(len(nums) - 2):
    #     for j in range(i + 1, len(nums)):
    #         for k in range(j + 1, len(nums)):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 l = sorted([nums[i], nums[j], nums[k]])
    #                 if l not in answer:
    #                     answer.append(l)
    #
    # return answer

    answer = []
    nums.sort()

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                answer.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return answer


print(threeSum([-1,0,1,2,-1,-4]))