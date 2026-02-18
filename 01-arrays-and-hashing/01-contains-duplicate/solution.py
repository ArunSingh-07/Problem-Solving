#BruteForce Method

def BF(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


#HashMap

def HM(nums:list[int])-> bool:
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
    ]

    for nums, expected in test_cases:
        # result = BF(nums)
        result = HM(nums)
        print(f"Input: {nums}, Expected: {expected}, Got: {result}")
        assert result == expected
    
    print("\nAll test cases passed!")
