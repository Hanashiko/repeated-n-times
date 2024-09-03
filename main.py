from typing import List, Dict

def repeatedNTimes(nums: List[int]) -> int:
    for i in nums:
        if nums.count(i) == int(len(nums) / 2):
            return i

def main() -> None:
    print(repeatedNTimes([1,2,3,3]))
    print(repeatedNTimes([2,1,2,5,3,2]))
    print(repeatedNTimes([5,1,5,2,5,3,5,4]))
    
if __name__ == "__main__":
    main()