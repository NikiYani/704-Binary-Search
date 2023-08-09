# 704. Binary Search

Given an array of integers nums which is sorted in ascending order, </br>
and an integer target, write a function to search target in nums. </br>
If target exists, then return its index. Otherwise, return -1. </br>

You must write an algorithm with O(log n) runtime complexity. </br>

## Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9 </br>
Output: 4 </br>
Explanation: 9 exists in nums and its index is 4 </br>

## Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2 </br>
Output: -1 </br>
Explanation: 2 does not exist in nums so return -1 </br>

## Constraints:

1 <= nums.length <= 104 </br>
-104 < nums[i], target < 104 </br>
All the integers in nums are unique. </br>
nums is sorted in ascending order. </br>