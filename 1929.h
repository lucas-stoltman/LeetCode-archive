// https://leetcode.com/problems/concatenation-of-array/
#pragma once

#include <iostream>

// begin solution
std::vector<int> getConcatenation(std::vector<int>& nums) {
   // hold previous size before it changes
   int size = nums.size();

   // add onto the vector
   for (int i = 0; i < size; i++) {
      nums.push_back(nums[i]);
   }
   return nums;
}
// end solution

void run1929() {

   std::cout << "1929: Concatenation of Array" << std::endl;
   std::vector<int> vect{2, 5, 2, 6, 3, 4, 6};

   std::cout << "Before:\t";
   for (int x : vect) {
      std::cout << x << " ";
   }
   std::cout << std::endl;

   std::cout << "After:\t";
   for (int x : getConcatenation(vect)) {
      std::cout << x << " ";
   }
   std::cout << std::endl;
}