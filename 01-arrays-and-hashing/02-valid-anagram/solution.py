from collections import Counter

# Hash Map Approach 
def isAnagram(s: str, t: str) -> bool:
 
    if len(s) != len(t):
        return False
    
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True


# python one Liner

def isAnagram1L(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# Brute Force
def BF(s:str, t:str) ->bool:
    if len(s)!=len(t):
        return False
    

    s_list = list(s)
    t_list = list(t)

    s_list.sort()
    t_list.sort()

    return s_list == t_list


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("", "", True),
        ("racecar", "carrace", True),
    ]

    methods = [
        ("Hash Map", isAnagram),
        # ("Sorting", isAnagramSorting),
        ("One Liner", isAnagram1L),
        ("Brute Force", BF)
    ]

    for name, method in methods:
        print(f"--- Testing {name} ---")
        for s, t, expected in test_cases:
            result = method(s, t)
            print(f"Input: s='{s}', t='{t}', Expected: {expected}, Got: {result}")
            assert result == expected
        print(f"{name} passed all tests!\n")
    
    print("All test cases passed successfully!")
