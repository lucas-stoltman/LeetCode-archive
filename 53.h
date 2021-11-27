// https://leetcode.com/problems/maximum-subarray/
#pragma once

#include <iostream>
#include <vector>

// begin solution
int maxSubArray(std::vector<int>& nums) {
   int currentSum = 0;
   int max = 0;

   if (nums.size() == 1) {
      return nums[0];
   } else {
      max = nums[0];
      for (int i = 0; i < nums.size(); i++) {
         currentSum += nums[i];

         // establish a max from the sum
         if (currentSum > max) {
            max = currentSum;
         }

         // establish a max from the array slot
         if (nums[i] > max) {
            max = nums[i];
         }

         // establish a new starting point
         if (currentSum < nums[i]) {
            currentSum = nums[i];
         }
      }
   }
   return max;
}

// end solution

void run53() {
   std::cout << "53: Maximum Subarray" << std::endl;
   std::vector<int> vect{-2, 5, 2, -6, 3, 4, 6, -2, 7};

   std::cout << "Before:\t";
   for (int x : vect) {
      std::cout << x << " ";
   }
   std::cout << std::endl;

   std::cout << "After:\t" << maxSubArray(vect);

   std::cout << std::endl;
}